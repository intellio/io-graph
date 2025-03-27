from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HardwareInformation(BaseModel):
	batteryChargeCycles: Optional[int] = Field(alias="batteryChargeCycles", default=None,)
	batteryHealthPercentage: Optional[int] = Field(alias="batteryHealthPercentage", default=None,)
	batteryLevelPercentage: float | str | ReferenceNumeric
	batterySerialNumber: Optional[str] = Field(alias="batterySerialNumber", default=None,)
	cellularTechnology: Optional[str] = Field(alias="cellularTechnology", default=None,)
	deviceFullQualifiedDomainName: Optional[str] = Field(alias="deviceFullQualifiedDomainName", default=None,)
	deviceGuardLocalSystemAuthorityCredentialGuardState: Optional[DeviceGuardLocalSystemAuthorityCredentialGuardState | str] = Field(alias="deviceGuardLocalSystemAuthorityCredentialGuardState", default=None,)
	deviceGuardVirtualizationBasedSecurityHardwareRequirementState: Optional[DeviceGuardVirtualizationBasedSecurityHardwareRequirementState | str] = Field(alias="deviceGuardVirtualizationBasedSecurityHardwareRequirementState", default=None,)
	deviceGuardVirtualizationBasedSecurityState: Optional[DeviceGuardVirtualizationBasedSecurityState | str] = Field(alias="deviceGuardVirtualizationBasedSecurityState", default=None,)
	deviceLicensingLastErrorCode: Optional[int] = Field(alias="deviceLicensingLastErrorCode", default=None,)
	deviceLicensingLastErrorDescription: Optional[str] = Field(alias="deviceLicensingLastErrorDescription", default=None,)
	deviceLicensingStatus: Optional[DeviceLicensingStatus | str] = Field(alias="deviceLicensingStatus", default=None,)
	esimIdentifier: Optional[str] = Field(alias="esimIdentifier", default=None,)
	freeStorageSpace: Optional[int] = Field(alias="freeStorageSpace", default=None,)
	imei: Optional[str] = Field(alias="imei", default=None,)
	ipAddressV4: Optional[str] = Field(alias="ipAddressV4", default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted", default=None,)
	isSharedDevice: Optional[bool] = Field(alias="isSharedDevice", default=None,)
	isSupervised: Optional[bool] = Field(alias="isSupervised", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	meid: Optional[str] = Field(alias="meid", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	operatingSystemEdition: Optional[str] = Field(alias="operatingSystemEdition", default=None,)
	operatingSystemLanguage: Optional[str] = Field(alias="operatingSystemLanguage", default=None,)
	operatingSystemProductType: Optional[int] = Field(alias="operatingSystemProductType", default=None,)
	osBuildNumber: Optional[str] = Field(alias="osBuildNumber", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	residentUsersCount: Optional[int] = Field(alias="residentUsersCount", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	sharedDeviceCachedUsers: Optional[list[SharedAppleDeviceUser]] = Field(alias="sharedDeviceCachedUsers", default=None,)
	subnetAddress: Optional[str] = Field(alias="subnetAddress", default=None,)
	subscriberCarrier: Optional[str] = Field(alias="subscriberCarrier", default=None,)
	systemManagementBIOSVersion: Optional[str] = Field(alias="systemManagementBIOSVersion", default=None,)
	totalStorageSpace: Optional[int] = Field(alias="totalStorageSpace", default=None,)
	tpmManufacturer: Optional[str] = Field(alias="tpmManufacturer", default=None,)
	tpmSpecificationVersion: Optional[str] = Field(alias="tpmSpecificationVersion", default=None,)
	tpmVersion: Optional[str] = Field(alias="tpmVersion", default=None,)
	wifiMac: Optional[str] = Field(alias="wifiMac", default=None,)
	wiredIPv4Addresses: Optional[list[str]] = Field(alias="wiredIPv4Addresses", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .device_guard_local_system_authority_credential_guard_state import DeviceGuardLocalSystemAuthorityCredentialGuardState
from .device_guard_virtualization_based_security_hardware_requirement_state import DeviceGuardVirtualizationBasedSecurityHardwareRequirementState
from .device_guard_virtualization_based_security_state import DeviceGuardVirtualizationBasedSecurityState
from .device_licensing_status import DeviceLicensingStatus
from .shared_apple_device_user import SharedAppleDeviceUser

