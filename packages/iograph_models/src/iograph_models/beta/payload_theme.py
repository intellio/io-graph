from __future__ import annotations
from enum import StrEnum


class PayloadTheme(StrEnum):
	unknown = "unknown"
	other = "other"
	accountActivation = "accountActivation"
	accountVerification = "accountVerification"
	billing = "billing"
	cleanUpMail = "cleanUpMail"
	controversial = "controversial"
	documentReceived = "documentReceived"
	expense = "expense"
	fax = "fax"
	financeReport = "financeReport"
	incomingMessages = "incomingMessages"
	invoice = "invoice"
	itemReceived = "itemReceived"
	loginAlert = "loginAlert"
	mailReceived = "mailReceived"
	password = "password"
	payment = "payment"
	payroll = "payroll"
	personalizedOffer = "personalizedOffer"
	quarantine = "quarantine"
	remoteWork = "remoteWork"
	reviewMessage = "reviewMessage"
	securityUpdate = "securityUpdate"
	serviceSuspended = "serviceSuspended"
	signatureRequired = "signatureRequired"
	upgradeMailboxStorage = "upgradeMailboxStorage"
	verifyMailbox = "verifyMailbox"
	voicemail = "voicemail"
	advertisement = "advertisement"
	employeeEngagement = "employeeEngagement"
	unknownFutureValue = "unknownFutureValue"

