from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionResultDetail(StrEnum):
	none = "none"
	underInvestigation = "underInvestigation"
	simulatedThreat = "simulatedThreat"
	allowedBySecOps = "allowedBySecOps"
	allowedByThirdPartyFilters = "allowedByThirdPartyFilters"
	messageNotFound = "messageNotFound"
	urlFileShouldNotBeBlocked = "urlFileShouldNotBeBlocked"
	urlFileShouldBeBlocked = "urlFileShouldBeBlocked"
	urlFileCannotMakeDecision = "urlFileCannotMakeDecision"
	domainImpersonation = "domainImpersonation"
	userImpersonation = "userImpersonation"
	brandImpersonation = "brandImpersonation"
	outboundShouldNotBeBlocked = "outboundShouldNotBeBlocked"
	outboundShouldBeBlocked = "outboundShouldBeBlocked"
	outboundBulk = "outboundBulk"
	outboundCannotMakeDecision = "outboundCannotMakeDecision"
	outboundNotRescanned = "outboundNotRescanned"
	zeroHourAutoPurgeAllowed = "zeroHourAutoPurgeAllowed"
	zeroHourAutoPurgeBlocked = "zeroHourAutoPurgeBlocked"
	zeroHourAutoPurgeQuarantineReleased = "zeroHourAutoPurgeQuarantineReleased"
	onPremisesSkip = "onPremisesSkip"
	allowedByTenantAllowBlockList = "allowedByTenantAllowBlockList"
	blockedByTenantAllowBlockList = "blockedByTenantAllowBlockList"
	allowedUrlByTenantAllowBlockList = "allowedUrlByTenantAllowBlockList"
	allowedFileByTenantAllowBlockList = "allowedFileByTenantAllowBlockList"
	allowedSenderByTenantAllowBlockList = "allowedSenderByTenantAllowBlockList"
	allowedRecipientByTenantAllowBlockList = "allowedRecipientByTenantAllowBlockList"
	blockedUrlByTenantAllowBlockList = "blockedUrlByTenantAllowBlockList"
	blockedFileByTenantAllowBlockList = "blockedFileByTenantAllowBlockList"
	blockedSenderByTenantAllowBlockList = "blockedSenderByTenantAllowBlockList"
	blockedRecipientByTenantAllowBlockList = "blockedRecipientByTenantAllowBlockList"
	allowedByConnection = "allowedByConnection"
	blockedByConnection = "blockedByConnection"
	allowedByExchangeTransportRule = "allowedByExchangeTransportRule"
	blockedByExchangeTransportRule = "blockedByExchangeTransportRule"
	quarantineReleased = "quarantineReleased"
	quarantineReleasedThenBlocked = "quarantineReleasedThenBlocked"
	junkMailRuleDisabled = "junkMailRuleDisabled"
	allowedByUserSetting = "allowedByUserSetting"
	blockedByUserSetting = "blockedByUserSetting"
	allowedByTenant = "allowedByTenant"
	blockedByTenant = "blockedByTenant"
	invalidFalsePositive = "invalidFalsePositive"
	invalidFalseNegative = "invalidFalseNegative"
	spoofBlocked = "spoofBlocked"
	goodReclassifiedAsBad = "goodReclassifiedAsBad"
	goodReclassifiedAsBulk = "goodReclassifiedAsBulk"
	goodReclassifiedAsGood = "goodReclassifiedAsGood"
	goodReclassifiedAsCannotMakeDecision = "goodReclassifiedAsCannotMakeDecision"
	badReclassifiedAsGood = "badReclassifiedAsGood"
	badReclassifiedAsBulk = "badReclassifiedAsBulk"
	badReclassifiedAsBad = "badReclassifiedAsBad"
	badReclassifiedAsCannotMakeDecision = "badReclassifiedAsCannotMakeDecision"
	unknownFutureValue = "unknownFutureValue"
	willNotifyOnceDone = "willNotifyOnceDone"
	checkUserReportedSettings = "checkUserReportedSettings"
	partOfEducationCampaign = "partOfEducationCampaign"
	allowedByAdvancedDelivery = "allowedByAdvancedDelivery"
	allowedByEnhancedFiltering = "allowedByEnhancedFiltering"
	itemDeleted = "itemDeleted"
	itemFoundClean = "itemFoundClean"
	itemFoundMalicious = "itemFoundMalicious"
	unableToMakeDecision = "unableToMakeDecision"
	domainResembledYourOrganization = "domainResembledYourOrganization"
	endUserBeingImpersonated = "endUserBeingImpersonated"
	associatedWithBrand = "associatedWithBrand"
	senderFailedAuthentication = "senderFailedAuthentication"
	endUserBeingSpoofed = "endUserBeingSpoofed"
	itemFoundBulk = "itemFoundBulk"
	itemNotReceivedByService = "itemNotReceivedByService"
	itemFoundSpam = "itemFoundSpam"

