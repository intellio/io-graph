from __future__ import annotations
from enum import StrEnum


class CloudPcStatus(StrEnum):
	notProvisioned = "notProvisioned"
	provisioning = "provisioning"
	provisioned = "provisioned"
	inGracePeriod = "inGracePeriod"
	deprovisioning = "deprovisioning"
	failed = "failed"
	provisionedWithWarnings = "provisionedWithWarnings"
	resizing = "resizing"
	restoring = "restoring"
	pendingProvision = "pendingProvision"
	unknownFutureValue = "unknownFutureValue"
	movingRegion = "movingRegion"
	resizePendingLicense = "resizePendingLicense"
	updatingSingleSignOn = "updatingSingleSignOn"
	modifyingSingleSignOn = "modifyingSingleSignOn"
	preparing = "preparing"

