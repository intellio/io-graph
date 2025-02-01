# generated by datamodel-codegen:
#   filename:  https://github.com/microsoftgraph/msgraph-metadata/raw/refs/heads/master/openapi/v1.0/openapi.yaml
#   timestamp: 2025-01-31T10:52:52+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from .... import (
    BaseCollectionPaginationCountResponse,
)
from .. import LongRunningOperationStatus, PublicError
from .. import Entity


class BilledReconciliation(Entity):
    field_odata_type: str


class BilledUsage(Entity):
    field_odata_type: str


class BillingReconciliation(Entity):
    billed: BilledReconciliation | None = None
    field_odata_type: str


class Operation(Entity):
    created_date_time: Annotated[
        datetime | None,
        Field(
            description='The start time of the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.',

        ),
    ] = None
    last_action_date_time: Annotated[
        datetime | None,
        Field(
            description='The time of the last action of the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.',

        ),
    ] = None
    status: Annotated[
        LongRunningOperationStatus | Dict[str, Any] | None,
        Field(
            description='The status of the operation. Possible values are: notStarted, running, completed, failed, unknownFutureValue.'
        ),
    ] = None
    field_odata_type: str


class RunningOperation(Operation):
    field_odata_type: str


class UnbilledUsage(Entity):
    field_odata_type: str


class Blob(BaseModel):
    name: Annotated[str | None, Field(description='The blob name.')] = None
    partition_value: Annotated[
        str | None,
        Field(
            description='The partition that contains the file. A large partition is split into multiple files, each with the same partitionValue.'
        ),
    ] = None
    field_odata_type: str


class AttributeSet(Enum):
    full = 'full'
    basic = 'basic'
    unknown_future_value = 'unknownFutureValue'


class BillingPeriod(Enum):
    current = 'current'
    last = 'last'
    unknown_future_value = 'unknownFutureValue'


class AzureUsage(Entity):
    billed: BilledUsage | None = None
    unbilled: UnbilledUsage | None = None
    field_odata_type: str


class FailedOperation(Operation):
    error: PublicError | None = None
    field_odata_type: str


class Manifest(Entity):
    blob_count: Annotated[
        float | None,
        Field(
            description='The total file count for this partner tenant ID.',
            ge=-2147483648.0,
            le=2147483647.0,
        ),
    ] = None
    blobs: Annotated[
        List[Blob] | None,
        Field(
            description='A collection of blob objects that contain details of all the files for the partner tenant ID.'
        ),
    ] = None
    created_date_time: Annotated[
        datetime | None,
        Field(
            description='The date and time when a manifest resource was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.',

        ),
    ] = None
    data_format: Annotated[
        str | None,
        Field(
            description='The billing data file format. The possible value is: compressedJSONLines. Each blob is a compressed file and data in the file is in JSON lines format. Decompress the file to access the data.'
        ),
    ] = None
    e_tag: Annotated[
        str | None,
        Field(
            description='Version of data represented by the manifest. Any change in eTag indicates a new data version.'
        ),
    ] = None
    partition_type: Annotated[
        str | None,
        Field(
            description='Indicates the division of data. If a given partition has more than the supported number, the data is split into multiple files, each file representing a specific partitionValue. By default, the data in the file is partitioned by the number of line items.'
        ),
    ] = None
    partner_tenant_id: Annotated[
        str | None, Field(description='The Microsoft Entra tenant ID of the partner.')
    ] = None
    root_directory: Annotated[
        str | None, Field(description='The root directory that contains all the files.')
    ] = None
    sas_token: Annotated[
        str | None,
        Field(
            description='The SAS token for accessing the directory or an individual file in the directory.'
        ),
    ] = None
    schema_version: Annotated[
        str | None, Field(description='The version of the manifest schema.')
    ] = None
    field_odata_type: str


class ManifestCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[Manifest] | None = None


class OperationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[Operation] | None = None


class FailedOperationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[FailedOperation] | None = None


class RunningOperationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[RunningOperation] | None = None


class BlobCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[Blob] | None = None


class Billing(Entity):
    manifests: Annotated[
        List[Manifest] | None,
        Field(description='Represents metadata for the exported data.'),
    ] = None
    operations: Annotated[
        List[Operation] | None,
        Field(
            description='Represents an operation to export the billing data of a partner.'
        ),
    ] = None
    reconciliation: BillingReconciliation | None = None
    usage: AzureUsage | None = None
    field_odata_type: str


class ExportSuccessOperation(Operation):
    resource_location: Manifest | None = None
    field_odata_type: str


class ExportSuccessOperationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: List[ExportSuccessOperation] | None = None
