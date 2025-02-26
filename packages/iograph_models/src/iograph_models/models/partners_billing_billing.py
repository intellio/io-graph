from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnersBillingBilling(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	manifests: list[PartnersBillingManifest] = Field(alias="manifests",)
	operations: list[PartnersBillingOperation] = Field(alias="operations",)
	reconciliation: Optional[PartnersBillingBillingReconciliation] = Field(default=None,alias="reconciliation",)
	usage: Optional[PartnersBillingAzureUsage] = Field(default=None,alias="usage",)

from .partners_billing_manifest import PartnersBillingManifest
from .partners_billing_operation import PartnersBillingOperation
from .partners_billing_billing_reconciliation import PartnersBillingBillingReconciliation
from .partners_billing_azure_usage import PartnersBillingAzureUsage

