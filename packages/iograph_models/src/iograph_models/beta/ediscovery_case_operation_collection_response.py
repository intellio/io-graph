from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCaseOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[EdiscoveryAddToReviewSetOperation, EdiscoveryCaseExportOperation, EdiscoveryCaseHoldOperation, EdiscoveryCaseIndexOperation, EdiscoveryEstimateStatisticsOperation, EdiscoveryPurgeDataOperation, EdiscoveryTagOperation]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
from .ediscovery_case_export_operation import EdiscoveryCaseExportOperation
from .ediscovery_case_hold_operation import EdiscoveryCaseHoldOperation
from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
from .ediscovery_tag_operation import EdiscoveryTagOperation

