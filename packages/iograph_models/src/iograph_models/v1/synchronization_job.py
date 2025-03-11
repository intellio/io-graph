from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJob(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	schedule: Optional[SynchronizationSchedule] = Field(alias="schedule",default=None,)
	status: Optional[SynchronizationStatus] = Field(alias="status",default=None,)
	synchronizationJobSettings: Optional[list[KeyValuePair]] = Field(alias="synchronizationJobSettings",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)
	bulkUpload: Optional[BulkUpload] = Field(alias="bulkUpload",default=None,)
	schema: Optional[SynchronizationSchema] = Field(alias="schema",default=None,)

from .synchronization_schedule import SynchronizationSchedule
from .synchronization_status import SynchronizationStatus
from .key_value_pair import KeyValuePair
from .bulk_upload import BulkUpload
from .synchronization_schema import SynchronizationSchema

