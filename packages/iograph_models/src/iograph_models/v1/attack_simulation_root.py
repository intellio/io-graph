from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttackSimulationRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endUserNotifications: Optional[list[EndUserNotification]] = Field(alias="endUserNotifications",default=None,)
	landingPages: Optional[list[LandingPage]] = Field(alias="landingPages",default=None,)
	loginPages: Optional[list[LoginPage]] = Field(alias="loginPages",default=None,)
	operations: Optional[list[AttackSimulationOperation]] = Field(alias="operations",default=None,)
	payloads: Optional[list[Payload]] = Field(alias="payloads",default=None,)
	simulationAutomations: Optional[list[SimulationAutomation]] = Field(alias="simulationAutomations",default=None,)
	simulations: Optional[list[Simulation]] = Field(alias="simulations",default=None,)
	trainings: Optional[list[Training]] = Field(alias="trainings",default=None,)

from .end_user_notification import EndUserNotification
from .landing_page import LandingPage
from .login_page import LoginPage
from .attack_simulation_operation import AttackSimulationOperation
from .payload import Payload
from .simulation_automation import SimulationAutomation
from .simulation import Simulation
from .training import Training

