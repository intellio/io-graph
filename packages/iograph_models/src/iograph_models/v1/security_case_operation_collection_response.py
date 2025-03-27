from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCaseOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityEdiscoveryAddToReviewSetOperation, SecurityEdiscoveryEstimateOperation, SecurityEdiscoveryExportOperation, SecurityEdiscoveryHoldOperation, SecurityEdiscoveryIndexOperation, SecurityEdiscoveryPurgeDataOperation, SecurityEdiscoverySearchExportOperation, SecurityEdiscoveryTagOperation]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
from .security_ediscovery_export_operation import SecurityEdiscoveryExportOperation
from .security_ediscovery_hold_operation import SecurityEdiscoveryHoldOperation
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
from .security_ediscovery_purge_data_operation import SecurityEdiscoveryPurgeDataOperation
from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation
from .security_ediscovery_tag_operation import SecurityEdiscoveryTagOperation

