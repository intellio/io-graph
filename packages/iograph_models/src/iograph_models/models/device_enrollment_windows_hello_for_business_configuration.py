from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceEnrollmentWindowsHelloForBusinessConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[EnrollmentConfigurationAssignment] = Field(alias="assignments",)
	enhancedBiometricsState: Optional[Enablement] = Field(default=None,alias="enhancedBiometricsState",)
	pinExpirationInDays: Optional[int] = Field(default=None,alias="pinExpirationInDays",)
	pinLowercaseCharactersUsage: Optional[WindowsHelloForBusinessPinUsage] = Field(default=None,alias="pinLowercaseCharactersUsage",)
	pinMaximumLength: Optional[int] = Field(default=None,alias="pinMaximumLength",)
	pinMinimumLength: Optional[int] = Field(default=None,alias="pinMinimumLength",)
	pinPreviousBlockCount: Optional[int] = Field(default=None,alias="pinPreviousBlockCount",)
	pinSpecialCharactersUsage: Optional[WindowsHelloForBusinessPinUsage] = Field(default=None,alias="pinSpecialCharactersUsage",)
	pinUppercaseCharactersUsage: Optional[WindowsHelloForBusinessPinUsage] = Field(default=None,alias="pinUppercaseCharactersUsage",)
	remotePassportEnabled: Optional[bool] = Field(default=None,alias="remotePassportEnabled",)
	securityDeviceRequired: Optional[bool] = Field(default=None,alias="securityDeviceRequired",)
	state: Optional[Enablement] = Field(default=None,alias="state",)
	unlockWithBiometricsEnabled: Optional[bool] = Field(default=None,alias="unlockWithBiometricsEnabled",)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .enablement import Enablement
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from .enablement import Enablement

