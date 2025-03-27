from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class LongRunningOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AttackSimulationOperation, EngagementAsyncOperation, GoalsExportJob, RichLongRunningOperation, IndustryDataValidateOperation, IndustryDataFileValidateOperation],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .attack_simulation_operation import AttackSimulationOperation
from .engagement_async_operation import EngagementAsyncOperation
from .goals_export_job import GoalsExportJob
from .rich_long_running_operation import RichLongRunningOperation
from .industry_data_validate_operation import IndustryDataValidateOperation
from .industry_data_file_validate_operation import IndustryDataFileValidateOperation

