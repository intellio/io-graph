from __future__ import annotations
from enum import StrEnum


class ConditionalAccessRule(StrEnum):
	allApps = "allApps"
	firstPartyApps = "firstPartyApps"
	office365 = "office365"
	appId = "appId"
	acr = "acr"
	appFilter = "appFilter"
	allUsers = "allUsers"
	guest = "guest"
	groupId = "groupId"
	roleId = "roleId"
	userId = "userId"
	allDevicePlatforms = "allDevicePlatforms"
	devicePlatform = "devicePlatform"
	allLocations = "allLocations"
	insideCorpnet = "insideCorpnet"
	allTrustedLocations = "allTrustedLocations"
	locationId = "locationId"
	allDevices = "allDevices"
	deviceFilter = "deviceFilter"
	deviceState = "deviceState"
	unknownFutureValue = "unknownFutureValue"
	deviceFilterIncludeRuleNotMatched = "deviceFilterIncludeRuleNotMatched"
	allDeviceStates = "allDeviceStates"
	anonymizedIPAddress = "anonymizedIPAddress"
	unfamiliarFeatures = "unfamiliarFeatures"
	nationStateIPAddress = "nationStateIPAddress"
	realTimeThreatIntelligence = "realTimeThreatIntelligence"
	internalGuest = "internalGuest"
	b2bCollaborationGuest = "b2bCollaborationGuest"
	b2bCollaborationMember = "b2bCollaborationMember"
	b2bDirectConnectUser = "b2bDirectConnectUser"
	otherExternalUser = "otherExternalUser"
	serviceProvider = "serviceProvider"
	microsoftAdminPortals = "microsoftAdminPortals"
	deviceCodeFlow = "deviceCodeFlow"
	authenticationTransfer = "authenticationTransfer"
	insiderRisk = "insiderRisk"

