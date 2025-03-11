from __future__ import annotations
from enum import StrEnum


class GroupPolicySettingType(StrEnum):
	unknown = "unknown"
	policy = "policy"
	account = "account"
	securityOptions = "securityOptions"
	userRightsAssignment = "userRightsAssignment"
	auditSetting = "auditSetting"
	windowsFirewallSettings = "windowsFirewallSettings"
	appLockerRuleCollection = "appLockerRuleCollection"
	dataSourcesSettings = "dataSourcesSettings"
	devicesSettings = "devicesSettings"
	driveMapSettings = "driveMapSettings"
	environmentVariables = "environmentVariables"
	filesSettings = "filesSettings"
	folderOptions = "folderOptions"
	folders = "folders"
	iniFiles = "iniFiles"
	internetOptions = "internetOptions"
	localUsersAndGroups = "localUsersAndGroups"
	networkOptions = "networkOptions"
	networkShares = "networkShares"
	ntServices = "ntServices"
	powerOptions = "powerOptions"
	printers = "printers"
	regionalOptionsSettings = "regionalOptionsSettings"
	registrySettings = "registrySettings"
	scheduledTasks = "scheduledTasks"
	shortcutSettings = "shortcutSettings"
	startMenuSettings = "startMenuSettings"

