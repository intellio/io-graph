from __future__ import annotations
from enum import StrEnum


class WindowsPrivacyDataCategory(StrEnum):
	notConfigured = "notConfigured"
	accountInfo = "accountInfo"
	appsRunInBackground = "appsRunInBackground"
	calendar = "calendar"
	callHistory = "callHistory"
	camera = "camera"
	contacts = "contacts"
	diagnosticsInfo = "diagnosticsInfo"
	email = "email"
	location = "location"
	messaging = "messaging"
	microphone = "microphone"
	motion = "motion"
	notifications = "notifications"
	phone = "phone"
	radios = "radios"
	tasks = "tasks"
	syncWithDevices = "syncWithDevices"
	trustedDevices = "trustedDevices"

