from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingBilling(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	manifests: Optional[list[PartnersBillingManifest]] = Field(alias="manifests", default=None,)
	operations: Optional[list[Annotated[Union[PartnersBillingExportSuccessOperation, PartnersBillingFailedOperation, PartnersBillingRunningOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	reconciliation: Optional[PartnersBillingBillingReconciliation] = Field(alias="reconciliation", default=None,)
	usage: Optional[PartnersBillingAzureUsage] = Field(alias="usage", default=None,)

from .partners_billing_manifest import PartnersBillingManifest
from .partners_billing_export_success_operation import PartnersBillingExportSuccessOperation
from .partners_billing_failed_operation import PartnersBillingFailedOperation
from .partners_billing_running_operation import PartnersBillingRunningOperation
from .partners_billing_billing_reconciliation import PartnersBillingBillingReconciliation
from .partners_billing_azure_usage import PartnersBillingAzureUsage

