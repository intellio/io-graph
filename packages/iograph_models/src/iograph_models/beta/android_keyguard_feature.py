from __future__ import annotations
from enum import StrEnum


class AndroidKeyguardFeature(StrEnum):
	notConfigured = "notConfigured"
	camera = "camera"
	notifications = "notifications"
	unredactedNotifications = "unredactedNotifications"
	trustAgents = "trustAgents"
	fingerprint = "fingerprint"
	remoteInput = "remoteInput"
	allFeatures = "allFeatures"
	face = "face"
	iris = "iris"
	biometrics = "biometrics"

