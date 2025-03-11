from __future__ import annotations
from enum import StrEnum


class SecurityAuditLogUserType(StrEnum):
	Regular = "Regular"
	Reserved = "Reserved"
	Admin = "Admin"
	DcAdmin = "DcAdmin"
	System = "System"
	Application = "Application"
	ServicePrincipal = "ServicePrincipal"
	CustomPolicy = "CustomPolicy"
	SystemPolicy = "SystemPolicy"
	PartnerTechnician = "PartnerTechnician"
	Guest = "Guest"
	unknownFutureValue = "unknownFutureValue"

