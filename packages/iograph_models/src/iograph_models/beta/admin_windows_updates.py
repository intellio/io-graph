from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminWindowsUpdates(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	catalog: Optional[WindowsUpdatesCatalog] = Field(alias="catalog",default=None,)
	deploymentAudiences: Optional[list[WindowsUpdatesDeploymentAudience]] = Field(alias="deploymentAudiences",default=None,)
	deployments: Optional[list[WindowsUpdatesDeployment]] = Field(alias="deployments",default=None,)
	products: Optional[list[WindowsUpdatesProduct]] = Field(alias="products",default=None,)
	resourceConnections: SerializeAsAny[Optional[list[WindowsUpdatesResourceConnection]]] = Field(alias="resourceConnections",default=None,)
	updatableAssets: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="updatableAssets",default=None,)
	updatePolicies: Optional[list[WindowsUpdatesUpdatePolicy]] = Field(alias="updatePolicies",default=None,)

from .windows_updates_catalog import WindowsUpdatesCatalog
from .windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience
from .windows_updates_deployment import WindowsUpdatesDeployment
from .windows_updates_product import WindowsUpdatesProduct
from .windows_updates_resource_connection import WindowsUpdatesResourceConnection
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from .windows_updates_update_policy import WindowsUpdatesUpdatePolicy

