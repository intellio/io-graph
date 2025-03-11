from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentWindowsHelloForBusinessConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceEnrollmentConfigurationType: Optional[DeviceEnrollmentConfigurationType | str] = Field(alias="deviceEnrollmentConfigurationType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments",default=None,)
	enhancedBiometricsState: Optional[Enablement | str] = Field(alias="enhancedBiometricsState",default=None,)
	enhancedSignInSecurity: Optional[int] = Field(alias="enhancedSignInSecurity",default=None,)
	pinExpirationInDays: Optional[int] = Field(alias="pinExpirationInDays",default=None,)
	pinLowercaseCharactersUsage: Optional[WindowsHelloForBusinessPinUsage | str] = Field(alias="pinLowercaseCharactersUsage",default=None,)
	pinMaximumLength: Optional[int] = Field(alias="pinMaximumLength",default=None,)
	pinMinimumLength: Optional[int] = Field(alias="pinMinimumLength",default=None,)
	pinPreviousBlockCount: Optional[int] = Field(alias="pinPreviousBlockCount",default=None,)
	pinSpecialCharactersUsage: Optional[WindowsHelloForBusinessPinUsage | str] = Field(alias="pinSpecialCharactersUsage",default=None,)
	pinUppercaseCharactersUsage: Optional[WindowsHelloForBusinessPinUsage | str] = Field(alias="pinUppercaseCharactersUsage",default=None,)
	remotePassportEnabled: Optional[bool] = Field(alias="remotePassportEnabled",default=None,)
	securityDeviceRequired: Optional[bool] = Field(alias="securityDeviceRequired",default=None,)
	securityKeyForSignIn: Optional[Enablement | str] = Field(alias="securityKeyForSignIn",default=None,)
	state: Optional[Enablement | str] = Field(alias="state",default=None,)
	unlockWithBiometricsEnabled: Optional[bool] = Field(alias="unlockWithBiometricsEnabled",default=None,)

from .device_enrollment_configuration_type import DeviceEnrollmentConfigurationType
from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .enablement import Enablement
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .enablement import Enablement
from .enablement import Enablement

