''
'' windows_firewall.vbs - Check for Check_MK
'' Original VBS NRPE script by Norman Bauer - Thanks! 
''
'' Modified by Maximilian Thoma for Check_MK plugin integration
'' 
''
'' This program is free software; you can redistribute it and/or modify it under the terms of the GNU
'' General Public License as published by the Free Software Foundation; either version 2 of the
'' License, or (at your option) any later version.
''
'' This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
'' even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
'' General Public License for more details.
''
'' You should have received a copy of the GNU General Public License along with this program; if not,
'' write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110, USA
''


Dim oStdOut, oShell, oFwMgr, oProfile, NET_FW_PROFILE_TYPE, objWshScriptExec, strLine, connState
On Error Resume Next

WScript.Echo("<<<windows_firewall>>>")

Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select * from Win32_OperatingSystem")
For Each objItem in colItems
  If InStr(objItem.Name, "Microsoft Windows Server 2003") > 0 Then
  	WScript.Echo("EMSG Windows Firewall will not be checked on " & objItem.Name)
  End If
Next 

Sub ExitWithUnknown()
  	WScript.Echo("EMSG Could not get Firewall State")
End Sub

Set oStdOut = WScript.StdOut
Set oShell = CreateObject("Wscript.Shell")
Set oFwMgr = CreateObject("HNetCfg.FwMgr")
Set oProfile = oFwMgr.LocalPolicy.CurrentProfile

NET_FW_PROFILE_TYPE = Array("Domain","Standard","Current","Unused","Unused")



If Err <> 0 Then
 	WScript.Echo("EMSG Windows Firewall Service not running")
	
End If

If oProfile.FirewallEnabled = False Then
	WScript.Echo("STATE OFF")
	WScript.Echo("PROFILE " & NET_FW_PROFILE_TYPE(oFwMgr.CurrentProfileType))
ElseIf oProfile.FirewallEnabled = True Then
	connState = ""
	Set objWshScriptExec = oShell.Exec("netsh advfirewall show currentprofile")
	Set oStdOut = objWshScriptExec.StdOut

	Do While Not oStdOut.AtEndOfStream
	   strLine = oStdOut.ReadLine
	   If InStr(strLine,"Firewall Policy") Then
	       connState = Replace(Lcase(Trim(Replace(strLine, "Firewall Policy", ""))), ",", ", ")
	       Exit Do
	   
	   ElseIf InStr(strLine,"Firewallrichtlinie") Then
	       connState = Replace(Lcase(Trim(Replace(strLine, "Firewallrichtlinie", ""))), ",", ", ")
	       Exit Do
	   End If
	   
	Loop
	
	if connState = "blockinbound, allowoutbound" Or connState = "eingehend blockieren, ausgehend zulassen" Then
  	WScript.Echo("STATE ON")
    WScript.Echo("PROFILE " & NET_FW_PROFILE_TYPE(oFwMgr.CurrentProfileType))
    WScript.Echo("CSTATE " & connState)
	else
  	WScript.Echo("STATE ON")
    WScript.Echo("PROFILE " & NET_FW_PROFILE_TYPE(oFwMgr.CurrentProfileType))
    WScript.Echo("CSTATE " & connState)
	End If	
Else
	ExitWithUnknown()
End If


Set oShell = Nothing
Set oFwMgr = Nothing
Set oProfile = Nothing
Set oStdOut = Nothing

