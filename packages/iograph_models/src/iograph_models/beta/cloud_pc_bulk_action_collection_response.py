from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[CloudPcBulkCreateSnapshot, CloudPcBulkDisasterRecoveryFailback, CloudPcBulkDisasterRecoveryFailover, CloudPcBulkModifyDiskEncryptionType, CloudPcBulkMove, CloudPcBulkPowerOff, CloudPcBulkPowerOn, CloudPcBulkReprovision, CloudPcBulkResize, CloudPcBulkRestart, CloudPcBulkRestore, CloudPcBulkSetReviewStatus, CloudPcBulkTroubleshoot],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
from .cloud_pc_bulk_move import CloudPcBulkMove
from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
from .cloud_pc_bulk_resize import CloudPcBulkResize
from .cloud_pc_bulk_restart import CloudPcBulkRestart
from .cloud_pc_bulk_restore import CloudPcBulkRestore
from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot

