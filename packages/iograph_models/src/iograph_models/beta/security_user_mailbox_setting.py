from __future__ import annotations
from enum import StrEnum


class SecurityUserMailboxSetting(StrEnum):
	none = "none"
	junkMailDeletion = "junkMailDeletion"
	isFromAddressInAddressBook = "isFromAddressInAddressBook"
	isFromAddressInAddressSafeList = "isFromAddressInAddressSafeList"
	isFromAddressInAddressBlockList = "isFromAddressInAddressBlockList"
	isFromAddressInAddressImplicitSafeList = "isFromAddressInAddressImplicitSafeList"
	isFromAddressInAddressImplicitJunkList = "isFromAddressInAddressImplicitJunkList"
	isFromDomainInDomainSafeList = "isFromDomainInDomainSafeList"
	isFromDomainInDomainBlockList = "isFromDomainInDomainBlockList"
	isRecipientInRecipientSafeList = "isRecipientInRecipientSafeList"
	customRule = "customRule"
	junkMailRule = "junkMailRule"
	senderPraPresent = "senderPraPresent"
	fromFirstTimeSender = "fromFirstTimeSender"
	exclusive = "exclusive"
	priorSeenPass = "priorSeenPass"
	senderAuthenticationSucceeded = "senderAuthenticationSucceeded"
	isJunkMailRuleEnabled = "isJunkMailRuleEnabled"
	unknownFutureValue = "unknownFutureValue"

