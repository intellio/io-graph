from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedDeviceEncryptionState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceEncryptionState"] = Field(alias="@odata.type",)
	advancedBitLockerStates: Optional[AdvancedBitLockerState | str] = Field(alias="advancedBitLockerStates", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceType: Optional[DeviceTypes | str] = Field(alias="deviceType", default=None,)
	encryptionPolicySettingState: Optional[ComplianceStatus | str] = Field(alias="encryptionPolicySettingState", default=None,)
	encryptionReadinessState: Optional[EncryptionReadinessState | str] = Field(alias="encryptionReadinessState", default=None,)
	encryptionState: Optional[EncryptionState | str] = Field(alias="encryptionState", default=None,)
	fileVaultStates: Optional[FileVaultState | str] = Field(alias="fileVaultStates", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	policyDetails: Optional[list[EncryptionReportPolicyDetails]] = Field(alias="policyDetails", default=None,)
	tpmSpecificationVersion: Optional[str] = Field(alias="tpmSpecificationVersion", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .advanced_bit_locker_state import AdvancedBitLockerState
from .device_types import DeviceTypes
from .compliance_status import ComplianceStatus
from .encryption_readiness_state import EncryptionReadinessState
from .encryption_state import EncryptionState
from .file_vault_state import FileVaultState
from .encryption_report_policy_details import EncryptionReportPolicyDetails
