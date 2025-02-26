# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .z__test import Z_TestRequest
	from .yield_mat import YieldMatRequest
	from .yield_disc import YieldDiscRequest
	from .yield import YieldRequest
	from .year_frac import YearFracRequest
	from .year import YearRequest
	from .xor import XorRequest
	from .xnpv import XnpvRequest
	from .xirr import XirrRequest
	from .work_day__intl import WorkDay_IntlRequest
	from .work_day import WorkDayRequest
	from .weibull__dist import Weibull_DistRequest
	from .week_num import WeekNumRequest
	from .weekday import WeekdayRequest
	from .vlookup import VlookupRequest
	from .vdb import VdbRequest
	from .var_p_a import VarPARequest
	from .var_a import VarARequest
	from .var__s import Var_SRequest
	from .var__p import Var_PRequest
	from .value import ValueRequest
	from .usdollar import UsdollarRequest
	from .upper import UpperRequest
	from .unicode import UnicodeRequest
	from .unichar import UnicharRequest
	from .type import TypeRequest
	from .trunc import TruncRequest
	from .true import TrueRequest
	from .trim_mean import TrimMeanRequest
	from .trim import TrimRequest
	from .today import TodayRequest
	from .timevalue import TimevalueRequest
	from .time import TimeRequest
	from .text import TextRequest
	from .tbill_yield import TbillYieldRequest
	from .tbill_price import TbillPriceRequest
	from .tbill_eq import TbillEqRequest
	from .tanh import TanhRequest
	from .tan import TanRequest
	from .t__inv_2_t import T_Inv_2TRequest
	from .t__inv import T_InvRequest
	from .t__dist__r_t import T_Dist_RTRequest
	from .t__dist_2_t import T_Dist_2TRequest
	from .t__dist import T_DistRequest
	from .t import TRequest
	from .syd import SydRequest
	from .sum_sq import SumSqRequest
	from .sum_ifs import SumIfsRequest
	from .sum_if import SumIfRequest
	from .sum import SumRequest
	from .subtotal import SubtotalRequest
	from .substitute import SubstituteRequest
	from .st_dev_p_a import StDevPARequest
	from .st_dev_a import StDevARequest
	from .st_dev__s import StDev_SRequest
	from .st_dev__p import StDev_PRequest
	from .standardize import StandardizeRequest
	from .sqrt_pi import SqrtPiRequest
	from .sqrt import SqrtRequest
	from .small import SmallRequest
	from .sln import SlnRequest
	from .skew_p import Skew_pRequest
	from .skew import SkewRequest
	from .sinh import SinhRequest
	from .sin import SinRequest
	from .sign import SignRequest
	from .sheets import SheetsRequest
	from .sheet import SheetRequest
	from .series_sum import SeriesSumRequest
	from .second import SecondRequest
	from .sech import SechRequest
	from .sec import SecRequest
	from .rri import RriRequest
	from .rows import RowsRequest
	from .round_up import RoundUpRequest
	from .round_down import RoundDownRequest
	from .round import RoundRequest
	from .roman import RomanRequest
	from .rightb import RightbRequest
	from .right import RightRequest
	from .rept import ReptRequest
	from .replace_b import ReplaceBRequest
	from .replace import ReplaceRequest
	from .received import ReceivedRequest
	from .rate import RateRequest
	from .rank__eq import Rank_EqRequest
	from .rank__avg import Rank_AvgRequest
	from .rand_between import RandBetweenRequest
	from .rand import RandRequest
	from .radians import RadiansRequest
	from .quotient import QuotientRequest
	from .quartile__inc import Quartile_IncRequest
	from .quartile__exc import Quartile_ExcRequest
	from .pv import PvRequest
	from .proper import ProperRequest
	from .product import ProductRequest
	from .price_mat import PriceMatRequest
	from .price_disc import PriceDiscRequest
	from .price import PriceRequest
	from .ppmt import PpmtRequest
	from .power import PowerRequest
	from .poisson__dist import Poisson_DistRequest
	from .pmt import PmtRequest
	from .pi import PiRequest
	from .phi import PhiRequest
	from .permutationa import PermutationaRequest
	from .permut import PermutRequest
	from .percent_rank__inc import PercentRank_IncRequest
	from .percent_rank__exc import PercentRank_ExcRequest
	from .percentile__inc import Percentile_IncRequest
	from .percentile__exc import Percentile_ExcRequest
	from .pduration import PdurationRequest
	from .or import OrRequest
	from .odd_l_yield import OddLYieldRequest
	from .odd_l_price import OddLPriceRequest
	from .odd_f_yield import OddFYieldRequest
	from .odd_f_price import OddFPriceRequest
	from .odd import OddRequest
	from .oct2_hex import Oct2HexRequest
	from .oct2_dec import Oct2DecRequest
	from .oct2_bin import Oct2BinRequest
	from .number_value import NumberValueRequest
	from .npv import NpvRequest
	from .nper import NperRequest
	from .now import NowRequest
	from .not import NotRequest
	from .norm__s__inv import Norm_S_InvRequest
	from .norm__s__dist import Norm_S_DistRequest
	from .norm__inv import Norm_InvRequest
	from .norm__dist import Norm_DistRequest
	from .nominal import NominalRequest
	from .network_days__intl import NetworkDays_IntlRequest
	from .network_days import NetworkDaysRequest
	from .neg_binom__dist import NegBinom_DistRequest
	from .na import NaRequest
	from .n import NRequest
	from .multi_nomial import MultiNomialRequest
	from .mround import MroundRequest
	from .month import MonthRequest
	from .mod import ModRequest
	from .mirr import MirrRequest
	from .minute import MinuteRequest
	from .min_a import MinARequest
	from .min import MinRequest
	from .midb import MidbRequest
	from .mid import MidRequest
	from .median import MedianRequest
	from .mduration import MdurationRequest
	from .max_a import MaxARequest
	from .max import MaxRequest
	from .match import MatchRequest
	from .lower import LowerRequest
	from .lookup import LookupRequest
	from .log_norm__inv import LogNorm_InvRequest
	from .log_norm__dist import LogNorm_DistRequest
	from .log10 import Log10Request
	from .log import LogRequest
	from .ln import LnRequest
	from .lenb import LenbRequest
	from .len import LenRequest
	from .leftb import LeftbRequest
	from .left import LeftRequest
	from .lcm import LcmRequest
	from .large import LargeRequest
	from .kurt import KurtRequest
	from .is_text import IsTextRequest
	from .isref import IsrefRequest
	from .ispmt import IspmtRequest
	from .iso_week_num import IsoWeekNumRequest
	from .is_odd import IsOddRequest
	from .iso__ceiling import Iso_CeilingRequest
	from .is_number import IsNumberRequest
	from .is_non_text import IsNonTextRequest
	from .is_n_a import IsNARequest
	from .is_logical import IsLogicalRequest
	from .is_formula import IsFormulaRequest
	from .is_even import IsEvenRequest
	from .is_error import IsErrorRequest
	from .is_err import IsErrRequest
	from .irr import IrrRequest
	from .ipmt import IpmtRequest
	from .int_rate import IntRateRequest
	from .int import IntRequest
	from .im_tan import ImTanRequest
	from .im_sum import ImSumRequest
	from .im_sub import ImSubRequest
	from .im_sqrt import ImSqrtRequest
	from .im_sinh import ImSinhRequest
	from .im_sin import ImSinRequest
	from .im_sech import ImSechRequest
	from .im_sec import ImSecRequest
	from .im_real import ImRealRequest
	from .im_product import ImProductRequest
	from .im_power import ImPowerRequest
	from .im_log2 import ImLog2Request
	from .im_log10 import ImLog10Request
	from .im_ln import ImLnRequest
	from .im_exp import ImExpRequest
	from .im_div import ImDivRequest
	from .im_csch import ImCschRequest
	from .im_csc import ImCscRequest
	from .im_cot import ImCotRequest
	from .im_cosh import ImCoshRequest
	from .im_cos import ImCosRequest
	from .im_conjugate import ImConjugateRequest
	from .im_argument import ImArgumentRequest
	from .imaginary import ImaginaryRequest
	from .im_abs import ImAbsRequest
	from .if import IfRequest
	from .hyp_geom__dist import HypGeom_DistRequest
	from .hyperlink import HyperlinkRequest
	from .hour import HourRequest
	from .hlookup import HlookupRequest
	from .hex2_oct import Hex2OctRequest
	from .hex2_dec import Hex2DecRequest
	from .hex2_bin import Hex2BinRequest
	from .har_mean import HarMeanRequest
	from .ge_step import GeStepRequest
	from .geo_mean import GeoMeanRequest
	from .gcd import GcdRequest
	from .gauss import GaussRequest
	from .gamma_ln__precise import GammaLn_PreciseRequest
	from .gamma_ln import GammaLnRequest
	from .gamma__inv import Gamma_InvRequest
	from .gamma__dist import Gamma_DistRequest
	from .gamma import GammaRequest
	from .fvschedule import FvscheduleRequest
	from .fv import FvRequest
	from .floor__precise import Floor_PreciseRequest
	from .floor__math import Floor_MathRequest
	from .fixed import FixedRequest
	from .fisher_inv import FisherInvRequest
	from .fisher import FisherRequest
	from .find_b import FindBRequest
	from .find import FindRequest
	from .false import FalseRequest
	from .fact_double import FactDoubleRequest
	from .fact import FactRequest
	from .f__inv__r_t import F_Inv_RTRequest
	from .f__inv import F_InvRequest
	from .f__dist__r_t import F_Dist_RTRequest
	from .f__dist import F_DistRequest
	from .expon__dist import Expon_DistRequest
	from .exp import ExpRequest
	from .exact import ExactRequest
	from .even import EvenRequest
	from .error__type import Error_TypeRequest
	from .erf_c__precise import ErfC_PreciseRequest
	from .erf_c import ErfCRequest
	from .erf__precise import Erf_PreciseRequest
	from .erf import ErfRequest
	from .eo_month import EoMonthRequest
	from .effect import EffectRequest
	from .edate import EdateRequest
	from .ecma__ceiling import Ecma_CeilingRequest
	from .dvar_p import DvarPRequest
	from .dvar import DvarRequest
	from .duration import DurationRequest
	from .dsum import DsumRequest
	from .dst_dev_p import DstDevPRequest
	from .dst_dev import DstDevRequest
	from .dproduct import DproductRequest
	from .dollar_fr import DollarFrRequest
	from .dollar_de import DollarDeRequest
	from .dollar import DollarRequest
	from .dmin import DminRequest
	from .dmax import DmaxRequest
	from .disc import DiscRequest
	from .dget import DgetRequest
	from .dev_sq import DevSqRequest
	from .delta import DeltaRequest
	from .degrees import DegreesRequest
	from .decimal import DecimalRequest
	from .dec2_oct import Dec2OctRequest
	from .dec2_hex import Dec2HexRequest
	from .dec2_bin import Dec2BinRequest
	from .ddb import DdbRequest
	from .dcount_a import DcountARequest
	from .dcount import DcountRequest
	from .dbcs import DbcsRequest
	from .db import DbRequest
	from .days360 import Days360Request
	from .days import DaysRequest
	from .day import DayRequest
	from .daverage import DaverageRequest
	from .datevalue import DatevalueRequest
	from .date import DateRequest
	from .cum_princ import CumPrincRequest
	from .cum_i_pmt import CumIPmtRequest
	from .csch import CschRequest
	from .csc import CscRequest
	from .coup_pcd import CoupPcdRequest
	from .coup_num import CoupNumRequest
	from .coup_ncd import CoupNcdRequest
	from .coup_days_nc import CoupDaysNcRequest
	from .coup_days import CoupDaysRequest
	from .coup_day_bs import CoupDayBsRequest
	from .count_ifs import CountIfsRequest
	from .count_if import CountIfRequest
	from .count_blank import CountBlankRequest
	from .count_a import CountARequest
	from .count import CountRequest
	from .coth import CothRequest
	from .cot import CotRequest
	from .cosh import CoshRequest
	from .cos import CosRequest
	from .convert import ConvertRequest
	from .confidence__t import Confidence_TRequest
	from .confidence__norm import Confidence_NormRequest
	from .concatenate import ConcatenateRequest
	from .complex import ComplexRequest
	from .combina import CombinaRequest
	from .combin import CombinRequest
	from .columns import ColumnsRequest
	from .code import CodeRequest
	from .clean import CleanRequest
	from .choose import ChooseRequest
	from .chi_sq__inv__r_t import ChiSq_Inv_RTRequest
	from .chi_sq__inv import ChiSq_InvRequest
	from .chi_sq__dist__r_t import ChiSq_Dist_RTRequest
	from .chi_sq__dist import ChiSq_DistRequest
	from .char import CharRequest
	from .ceiling__precise import Ceiling_PreciseRequest
	from .ceiling__math import Ceiling_MathRequest
	from .bitxor import BitxorRequest
	from .bitrshift import BitrshiftRequest
	from .bitor import BitorRequest
	from .bitlshift import BitlshiftRequest
	from .bitand import BitandRequest
	from .binom__inv import Binom_InvRequest
	from .binom__dist__range import Binom_Dist_RangeRequest
	from .binom__dist import Binom_DistRequest
	from .bin2_oct import Bin2OctRequest
	from .bin2_hex import Bin2HexRequest
	from .bin2_dec import Bin2DecRequest
	from .beta__inv import Beta_InvRequest
	from .beta__dist import Beta_DistRequest
	from .bessel_y import BesselYRequest
	from .bessel_k import BesselKRequest
	from .bessel_j import BesselJRequest
	from .bessel_i import BesselIRequest
	from .base import BaseRequest
	from .baht_text import BahtTextRequest
	from .average_ifs import AverageIfsRequest
	from .average_if import AverageIfRequest
	from .average_a import AverageARequest
	from .average import AverageRequest
	from .ave_dev import AveDevRequest
	from .atanh import AtanhRequest
	from .atan2 import Atan2Request
	from .atan import AtanRequest
	from .asinh import AsinhRequest
	from .asin import AsinRequest
	from .asc import AscRequest
	from .areas import AreasRequest
	from .arabic import ArabicRequest
	from .and import AndRequest
	from .amor_linc import AmorLincRequest
	from .amor_degrc import AmorDegrcRequest
	from .acoth import AcothRequest
	from .acot import AcotRequest
	from .acosh import AcoshRequest
	from .acos import AcosRequest
	from .accr_int_m import AccrIntMRequest
	from .accr_int import AccrIntRequest
	from .abs import AbsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_functions import WorkbookFunctions


class FunctionsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/functions"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookFunctions:
		"""
		Get functions from drives
		
		"""
		tags = ['drives.driveItem']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)

	async def patch(
		self,
		body: WorkbookFunctions,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookFunctions:
		"""
		Update the navigation property functions in drives
		
		"""
		tags = ['drives.driveItem']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property functions for drives
		
		"""
		tags = ['drives.driveItem']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	@property
	def abs(self,
	) -> AbsRequest:
		from .abs import AbsRequest
		return AbsRequest(self.request_adapter, self.path_parameters)

	@property
	def accr_int(self,
	) -> AccrIntRequest:
		from .accr_int import AccrIntRequest
		return AccrIntRequest(self.request_adapter, self.path_parameters)

	@property
	def accr_int_m(self,
	) -> AccrIntMRequest:
		from .accr_int_m import AccrIntMRequest
		return AccrIntMRequest(self.request_adapter, self.path_parameters)

	@property
	def acos(self,
	) -> AcosRequest:
		from .acos import AcosRequest
		return AcosRequest(self.request_adapter, self.path_parameters)

	@property
	def acosh(self,
	) -> AcoshRequest:
		from .acosh import AcoshRequest
		return AcoshRequest(self.request_adapter, self.path_parameters)

	@property
	def acot(self,
	) -> AcotRequest:
		from .acot import AcotRequest
		return AcotRequest(self.request_adapter, self.path_parameters)

	@property
	def acoth(self,
	) -> AcothRequest:
		from .acoth import AcothRequest
		return AcothRequest(self.request_adapter, self.path_parameters)

	@property
	def amor_degrc(self,
	) -> AmorDegrcRequest:
		from .amor_degrc import AmorDegrcRequest
		return AmorDegrcRequest(self.request_adapter, self.path_parameters)

	@property
	def amor_linc(self,
	) -> AmorLincRequest:
		from .amor_linc import AmorLincRequest
		return AmorLincRequest(self.request_adapter, self.path_parameters)

	@property
	def and(self,
	) -> AndRequest:
		from .and import AndRequest
		return AndRequest(self.request_adapter, self.path_parameters)

	@property
	def arabic(self,
	) -> ArabicRequest:
		from .arabic import ArabicRequest
		return ArabicRequest(self.request_adapter, self.path_parameters)

	@property
	def areas(self,
	) -> AreasRequest:
		from .areas import AreasRequest
		return AreasRequest(self.request_adapter, self.path_parameters)

	@property
	def asc(self,
	) -> AscRequest:
		from .asc import AscRequest
		return AscRequest(self.request_adapter, self.path_parameters)

	@property
	def asin(self,
	) -> AsinRequest:
		from .asin import AsinRequest
		return AsinRequest(self.request_adapter, self.path_parameters)

	@property
	def asinh(self,
	) -> AsinhRequest:
		from .asinh import AsinhRequest
		return AsinhRequest(self.request_adapter, self.path_parameters)

	@property
	def atan(self,
	) -> AtanRequest:
		from .atan import AtanRequest
		return AtanRequest(self.request_adapter, self.path_parameters)

	@property
	def atan2(self,
	) -> Atan2Request:
		from .atan2 import Atan2Request
		return Atan2Request(self.request_adapter, self.path_parameters)

	@property
	def atanh(self,
	) -> AtanhRequest:
		from .atanh import AtanhRequest
		return AtanhRequest(self.request_adapter, self.path_parameters)

	@property
	def ave_dev(self,
	) -> AveDevRequest:
		from .ave_dev import AveDevRequest
		return AveDevRequest(self.request_adapter, self.path_parameters)

	@property
	def average(self,
	) -> AverageRequest:
		from .average import AverageRequest
		return AverageRequest(self.request_adapter, self.path_parameters)

	@property
	def average_a(self,
	) -> AverageARequest:
		from .average_a import AverageARequest
		return AverageARequest(self.request_adapter, self.path_parameters)

	@property
	def average_if(self,
	) -> AverageIfRequest:
		from .average_if import AverageIfRequest
		return AverageIfRequest(self.request_adapter, self.path_parameters)

	@property
	def average_ifs(self,
	) -> AverageIfsRequest:
		from .average_ifs import AverageIfsRequest
		return AverageIfsRequest(self.request_adapter, self.path_parameters)

	@property
	def baht_text(self,
	) -> BahtTextRequest:
		from .baht_text import BahtTextRequest
		return BahtTextRequest(self.request_adapter, self.path_parameters)

	@property
	def base(self,
	) -> BaseRequest:
		from .base import BaseRequest
		return BaseRequest(self.request_adapter, self.path_parameters)

	@property
	def bessel_i(self,
	) -> BesselIRequest:
		from .bessel_i import BesselIRequest
		return BesselIRequest(self.request_adapter, self.path_parameters)

	@property
	def bessel_j(self,
	) -> BesselJRequest:
		from .bessel_j import BesselJRequest
		return BesselJRequest(self.request_adapter, self.path_parameters)

	@property
	def bessel_k(self,
	) -> BesselKRequest:
		from .bessel_k import BesselKRequest
		return BesselKRequest(self.request_adapter, self.path_parameters)

	@property
	def bessel_y(self,
	) -> BesselYRequest:
		from .bessel_y import BesselYRequest
		return BesselYRequest(self.request_adapter, self.path_parameters)

	@property
	def beta__dist(self,
	) -> Beta_DistRequest:
		from .beta__dist import Beta_DistRequest
		return Beta_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def beta__inv(self,
	) -> Beta_InvRequest:
		from .beta__inv import Beta_InvRequest
		return Beta_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def bin2_dec(self,
	) -> Bin2DecRequest:
		from .bin2_dec import Bin2DecRequest
		return Bin2DecRequest(self.request_adapter, self.path_parameters)

	@property
	def bin2_hex(self,
	) -> Bin2HexRequest:
		from .bin2_hex import Bin2HexRequest
		return Bin2HexRequest(self.request_adapter, self.path_parameters)

	@property
	def bin2_oct(self,
	) -> Bin2OctRequest:
		from .bin2_oct import Bin2OctRequest
		return Bin2OctRequest(self.request_adapter, self.path_parameters)

	@property
	def binom__dist(self,
	) -> Binom_DistRequest:
		from .binom__dist import Binom_DistRequest
		return Binom_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def binom__dist__range(self,
	) -> Binom_Dist_RangeRequest:
		from .binom__dist__range import Binom_Dist_RangeRequest
		return Binom_Dist_RangeRequest(self.request_adapter, self.path_parameters)

	@property
	def binom__inv(self,
	) -> Binom_InvRequest:
		from .binom__inv import Binom_InvRequest
		return Binom_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def bitand(self,
	) -> BitandRequest:
		from .bitand import BitandRequest
		return BitandRequest(self.request_adapter, self.path_parameters)

	@property
	def bitlshift(self,
	) -> BitlshiftRequest:
		from .bitlshift import BitlshiftRequest
		return BitlshiftRequest(self.request_adapter, self.path_parameters)

	@property
	def bitor(self,
	) -> BitorRequest:
		from .bitor import BitorRequest
		return BitorRequest(self.request_adapter, self.path_parameters)

	@property
	def bitrshift(self,
	) -> BitrshiftRequest:
		from .bitrshift import BitrshiftRequest
		return BitrshiftRequest(self.request_adapter, self.path_parameters)

	@property
	def bitxor(self,
	) -> BitxorRequest:
		from .bitxor import BitxorRequest
		return BitxorRequest(self.request_adapter, self.path_parameters)

	@property
	def ceiling__math(self,
	) -> Ceiling_MathRequest:
		from .ceiling__math import Ceiling_MathRequest
		return Ceiling_MathRequest(self.request_adapter, self.path_parameters)

	@property
	def ceiling__precise(self,
	) -> Ceiling_PreciseRequest:
		from .ceiling__precise import Ceiling_PreciseRequest
		return Ceiling_PreciseRequest(self.request_adapter, self.path_parameters)

	@property
	def char(self,
	) -> CharRequest:
		from .char import CharRequest
		return CharRequest(self.request_adapter, self.path_parameters)

	@property
	def chi_sq__dist(self,
	) -> ChiSq_DistRequest:
		from .chi_sq__dist import ChiSq_DistRequest
		return ChiSq_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def chi_sq__dist__r_t(self,
	) -> ChiSq_Dist_RTRequest:
		from .chi_sq__dist__r_t import ChiSq_Dist_RTRequest
		return ChiSq_Dist_RTRequest(self.request_adapter, self.path_parameters)

	@property
	def chi_sq__inv(self,
	) -> ChiSq_InvRequest:
		from .chi_sq__inv import ChiSq_InvRequest
		return ChiSq_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def chi_sq__inv__r_t(self,
	) -> ChiSq_Inv_RTRequest:
		from .chi_sq__inv__r_t import ChiSq_Inv_RTRequest
		return ChiSq_Inv_RTRequest(self.request_adapter, self.path_parameters)

	@property
	def choose(self,
	) -> ChooseRequest:
		from .choose import ChooseRequest
		return ChooseRequest(self.request_adapter, self.path_parameters)

	@property
	def clean(self,
	) -> CleanRequest:
		from .clean import CleanRequest
		return CleanRequest(self.request_adapter, self.path_parameters)

	@property
	def code(self,
	) -> CodeRequest:
		from .code import CodeRequest
		return CodeRequest(self.request_adapter, self.path_parameters)

	@property
	def columns(self,
	) -> ColumnsRequest:
		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, self.path_parameters)

	@property
	def combin(self,
	) -> CombinRequest:
		from .combin import CombinRequest
		return CombinRequest(self.request_adapter, self.path_parameters)

	@property
	def combina(self,
	) -> CombinaRequest:
		from .combina import CombinaRequest
		return CombinaRequest(self.request_adapter, self.path_parameters)

	@property
	def complex(self,
	) -> ComplexRequest:
		from .complex import ComplexRequest
		return ComplexRequest(self.request_adapter, self.path_parameters)

	@property
	def concatenate(self,
	) -> ConcatenateRequest:
		from .concatenate import ConcatenateRequest
		return ConcatenateRequest(self.request_adapter, self.path_parameters)

	@property
	def confidence__norm(self,
	) -> Confidence_NormRequest:
		from .confidence__norm import Confidence_NormRequest
		return Confidence_NormRequest(self.request_adapter, self.path_parameters)

	@property
	def confidence__t(self,
	) -> Confidence_TRequest:
		from .confidence__t import Confidence_TRequest
		return Confidence_TRequest(self.request_adapter, self.path_parameters)

	@property
	def convert(self,
	) -> ConvertRequest:
		from .convert import ConvertRequest
		return ConvertRequest(self.request_adapter, self.path_parameters)

	@property
	def cos(self,
	) -> CosRequest:
		from .cos import CosRequest
		return CosRequest(self.request_adapter, self.path_parameters)

	@property
	def cosh(self,
	) -> CoshRequest:
		from .cosh import CoshRequest
		return CoshRequest(self.request_adapter, self.path_parameters)

	@property
	def cot(self,
	) -> CotRequest:
		from .cot import CotRequest
		return CotRequest(self.request_adapter, self.path_parameters)

	@property
	def coth(self,
	) -> CothRequest:
		from .coth import CothRequest
		return CothRequest(self.request_adapter, self.path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def count_a(self,
	) -> CountARequest:
		from .count_a import CountARequest
		return CountARequest(self.request_adapter, self.path_parameters)

	@property
	def count_blank(self,
	) -> CountBlankRequest:
		from .count_blank import CountBlankRequest
		return CountBlankRequest(self.request_adapter, self.path_parameters)

	@property
	def count_if(self,
	) -> CountIfRequest:
		from .count_if import CountIfRequest
		return CountIfRequest(self.request_adapter, self.path_parameters)

	@property
	def count_ifs(self,
	) -> CountIfsRequest:
		from .count_ifs import CountIfsRequest
		return CountIfsRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_day_bs(self,
	) -> CoupDayBsRequest:
		from .coup_day_bs import CoupDayBsRequest
		return CoupDayBsRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_days(self,
	) -> CoupDaysRequest:
		from .coup_days import CoupDaysRequest
		return CoupDaysRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_days_nc(self,
	) -> CoupDaysNcRequest:
		from .coup_days_nc import CoupDaysNcRequest
		return CoupDaysNcRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_ncd(self,
	) -> CoupNcdRequest:
		from .coup_ncd import CoupNcdRequest
		return CoupNcdRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_num(self,
	) -> CoupNumRequest:
		from .coup_num import CoupNumRequest
		return CoupNumRequest(self.request_adapter, self.path_parameters)

	@property
	def coup_pcd(self,
	) -> CoupPcdRequest:
		from .coup_pcd import CoupPcdRequest
		return CoupPcdRequest(self.request_adapter, self.path_parameters)

	@property
	def csc(self,
	) -> CscRequest:
		from .csc import CscRequest
		return CscRequest(self.request_adapter, self.path_parameters)

	@property
	def csch(self,
	) -> CschRequest:
		from .csch import CschRequest
		return CschRequest(self.request_adapter, self.path_parameters)

	@property
	def cum_i_pmt(self,
	) -> CumIPmtRequest:
		from .cum_i_pmt import CumIPmtRequest
		return CumIPmtRequest(self.request_adapter, self.path_parameters)

	@property
	def cum_princ(self,
	) -> CumPrincRequest:
		from .cum_princ import CumPrincRequest
		return CumPrincRequest(self.request_adapter, self.path_parameters)

	@property
	def date(self,
	) -> DateRequest:
		from .date import DateRequest
		return DateRequest(self.request_adapter, self.path_parameters)

	@property
	def datevalue(self,
	) -> DatevalueRequest:
		from .datevalue import DatevalueRequest
		return DatevalueRequest(self.request_adapter, self.path_parameters)

	@property
	def daverage(self,
	) -> DaverageRequest:
		from .daverage import DaverageRequest
		return DaverageRequest(self.request_adapter, self.path_parameters)

	@property
	def day(self,
	) -> DayRequest:
		from .day import DayRequest
		return DayRequest(self.request_adapter, self.path_parameters)

	@property
	def days(self,
	) -> DaysRequest:
		from .days import DaysRequest
		return DaysRequest(self.request_adapter, self.path_parameters)

	@property
	def days360(self,
	) -> Days360Request:
		from .days360 import Days360Request
		return Days360Request(self.request_adapter, self.path_parameters)

	@property
	def db(self,
	) -> DbRequest:
		from .db import DbRequest
		return DbRequest(self.request_adapter, self.path_parameters)

	@property
	def dbcs(self,
	) -> DbcsRequest:
		from .dbcs import DbcsRequest
		return DbcsRequest(self.request_adapter, self.path_parameters)

	@property
	def dcount(self,
	) -> DcountRequest:
		from .dcount import DcountRequest
		return DcountRequest(self.request_adapter, self.path_parameters)

	@property
	def dcount_a(self,
	) -> DcountARequest:
		from .dcount_a import DcountARequest
		return DcountARequest(self.request_adapter, self.path_parameters)

	@property
	def ddb(self,
	) -> DdbRequest:
		from .ddb import DdbRequest
		return DdbRequest(self.request_adapter, self.path_parameters)

	@property
	def dec2_bin(self,
	) -> Dec2BinRequest:
		from .dec2_bin import Dec2BinRequest
		return Dec2BinRequest(self.request_adapter, self.path_parameters)

	@property
	def dec2_hex(self,
	) -> Dec2HexRequest:
		from .dec2_hex import Dec2HexRequest
		return Dec2HexRequest(self.request_adapter, self.path_parameters)

	@property
	def dec2_oct(self,
	) -> Dec2OctRequest:
		from .dec2_oct import Dec2OctRequest
		return Dec2OctRequest(self.request_adapter, self.path_parameters)

	@property
	def decimal(self,
	) -> DecimalRequest:
		from .decimal import DecimalRequest
		return DecimalRequest(self.request_adapter, self.path_parameters)

	@property
	def degrees(self,
	) -> DegreesRequest:
		from .degrees import DegreesRequest
		return DegreesRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

	@property
	def dev_sq(self,
	) -> DevSqRequest:
		from .dev_sq import DevSqRequest
		return DevSqRequest(self.request_adapter, self.path_parameters)

	@property
	def dget(self,
	) -> DgetRequest:
		from .dget import DgetRequest
		return DgetRequest(self.request_adapter, self.path_parameters)

	@property
	def disc(self,
	) -> DiscRequest:
		from .disc import DiscRequest
		return DiscRequest(self.request_adapter, self.path_parameters)

	@property
	def dmax(self,
	) -> DmaxRequest:
		from .dmax import DmaxRequest
		return DmaxRequest(self.request_adapter, self.path_parameters)

	@property
	def dmin(self,
	) -> DminRequest:
		from .dmin import DminRequest
		return DminRequest(self.request_adapter, self.path_parameters)

	@property
	def dollar(self,
	) -> DollarRequest:
		from .dollar import DollarRequest
		return DollarRequest(self.request_adapter, self.path_parameters)

	@property
	def dollar_de(self,
	) -> DollarDeRequest:
		from .dollar_de import DollarDeRequest
		return DollarDeRequest(self.request_adapter, self.path_parameters)

	@property
	def dollar_fr(self,
	) -> DollarFrRequest:
		from .dollar_fr import DollarFrRequest
		return DollarFrRequest(self.request_adapter, self.path_parameters)

	@property
	def dproduct(self,
	) -> DproductRequest:
		from .dproduct import DproductRequest
		return DproductRequest(self.request_adapter, self.path_parameters)

	@property
	def dst_dev(self,
	) -> DstDevRequest:
		from .dst_dev import DstDevRequest
		return DstDevRequest(self.request_adapter, self.path_parameters)

	@property
	def dst_dev_p(self,
	) -> DstDevPRequest:
		from .dst_dev_p import DstDevPRequest
		return DstDevPRequest(self.request_adapter, self.path_parameters)

	@property
	def dsum(self,
	) -> DsumRequest:
		from .dsum import DsumRequest
		return DsumRequest(self.request_adapter, self.path_parameters)

	@property
	def duration(self,
	) -> DurationRequest:
		from .duration import DurationRequest
		return DurationRequest(self.request_adapter, self.path_parameters)

	@property
	def dvar(self,
	) -> DvarRequest:
		from .dvar import DvarRequest
		return DvarRequest(self.request_adapter, self.path_parameters)

	@property
	def dvar_p(self,
	) -> DvarPRequest:
		from .dvar_p import DvarPRequest
		return DvarPRequest(self.request_adapter, self.path_parameters)

	@property
	def ecma__ceiling(self,
	) -> Ecma_CeilingRequest:
		from .ecma__ceiling import Ecma_CeilingRequest
		return Ecma_CeilingRequest(self.request_adapter, self.path_parameters)

	@property
	def edate(self,
	) -> EdateRequest:
		from .edate import EdateRequest
		return EdateRequest(self.request_adapter, self.path_parameters)

	@property
	def effect(self,
	) -> EffectRequest:
		from .effect import EffectRequest
		return EffectRequest(self.request_adapter, self.path_parameters)

	@property
	def eo_month(self,
	) -> EoMonthRequest:
		from .eo_month import EoMonthRequest
		return EoMonthRequest(self.request_adapter, self.path_parameters)

	@property
	def erf(self,
	) -> ErfRequest:
		from .erf import ErfRequest
		return ErfRequest(self.request_adapter, self.path_parameters)

	@property
	def erf__precise(self,
	) -> Erf_PreciseRequest:
		from .erf__precise import Erf_PreciseRequest
		return Erf_PreciseRequest(self.request_adapter, self.path_parameters)

	@property
	def erf_c(self,
	) -> ErfCRequest:
		from .erf_c import ErfCRequest
		return ErfCRequest(self.request_adapter, self.path_parameters)

	@property
	def erf_c__precise(self,
	) -> ErfC_PreciseRequest:
		from .erf_c__precise import ErfC_PreciseRequest
		return ErfC_PreciseRequest(self.request_adapter, self.path_parameters)

	@property
	def error__type(self,
	) -> Error_TypeRequest:
		from .error__type import Error_TypeRequest
		return Error_TypeRequest(self.request_adapter, self.path_parameters)

	@property
	def even(self,
	) -> EvenRequest:
		from .even import EvenRequest
		return EvenRequest(self.request_adapter, self.path_parameters)

	@property
	def exact(self,
	) -> ExactRequest:
		from .exact import ExactRequest
		return ExactRequest(self.request_adapter, self.path_parameters)

	@property
	def exp(self,
	) -> ExpRequest:
		from .exp import ExpRequest
		return ExpRequest(self.request_adapter, self.path_parameters)

	@property
	def expon__dist(self,
	) -> Expon_DistRequest:
		from .expon__dist import Expon_DistRequest
		return Expon_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def f__dist(self,
	) -> F_DistRequest:
		from .f__dist import F_DistRequest
		return F_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def f__dist__r_t(self,
	) -> F_Dist_RTRequest:
		from .f__dist__r_t import F_Dist_RTRequest
		return F_Dist_RTRequest(self.request_adapter, self.path_parameters)

	@property
	def f__inv(self,
	) -> F_InvRequest:
		from .f__inv import F_InvRequest
		return F_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def f__inv__r_t(self,
	) -> F_Inv_RTRequest:
		from .f__inv__r_t import F_Inv_RTRequest
		return F_Inv_RTRequest(self.request_adapter, self.path_parameters)

	@property
	def fact(self,
	) -> FactRequest:
		from .fact import FactRequest
		return FactRequest(self.request_adapter, self.path_parameters)

	@property
	def fact_double(self,
	) -> FactDoubleRequest:
		from .fact_double import FactDoubleRequest
		return FactDoubleRequest(self.request_adapter, self.path_parameters)

	@property
	def false(self,
	) -> FalseRequest:
		from .false import FalseRequest
		return FalseRequest(self.request_adapter, self.path_parameters)

	@property
	def find(self,
	) -> FindRequest:
		from .find import FindRequest
		return FindRequest(self.request_adapter, self.path_parameters)

	@property
	def find_b(self,
	) -> FindBRequest:
		from .find_b import FindBRequest
		return FindBRequest(self.request_adapter, self.path_parameters)

	@property
	def fisher(self,
	) -> FisherRequest:
		from .fisher import FisherRequest
		return FisherRequest(self.request_adapter, self.path_parameters)

	@property
	def fisher_inv(self,
	) -> FisherInvRequest:
		from .fisher_inv import FisherInvRequest
		return FisherInvRequest(self.request_adapter, self.path_parameters)

	@property
	def fixed(self,
	) -> FixedRequest:
		from .fixed import FixedRequest
		return FixedRequest(self.request_adapter, self.path_parameters)

	@property
	def floor__math(self,
	) -> Floor_MathRequest:
		from .floor__math import Floor_MathRequest
		return Floor_MathRequest(self.request_adapter, self.path_parameters)

	@property
	def floor__precise(self,
	) -> Floor_PreciseRequest:
		from .floor__precise import Floor_PreciseRequest
		return Floor_PreciseRequest(self.request_adapter, self.path_parameters)

	@property
	def fv(self,
	) -> FvRequest:
		from .fv import FvRequest
		return FvRequest(self.request_adapter, self.path_parameters)

	@property
	def fvschedule(self,
	) -> FvscheduleRequest:
		from .fvschedule import FvscheduleRequest
		return FvscheduleRequest(self.request_adapter, self.path_parameters)

	@property
	def gamma(self,
	) -> GammaRequest:
		from .gamma import GammaRequest
		return GammaRequest(self.request_adapter, self.path_parameters)

	@property
	def gamma__dist(self,
	) -> Gamma_DistRequest:
		from .gamma__dist import Gamma_DistRequest
		return Gamma_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def gamma__inv(self,
	) -> Gamma_InvRequest:
		from .gamma__inv import Gamma_InvRequest
		return Gamma_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def gamma_ln(self,
	) -> GammaLnRequest:
		from .gamma_ln import GammaLnRequest
		return GammaLnRequest(self.request_adapter, self.path_parameters)

	@property
	def gamma_ln__precise(self,
	) -> GammaLn_PreciseRequest:
		from .gamma_ln__precise import GammaLn_PreciseRequest
		return GammaLn_PreciseRequest(self.request_adapter, self.path_parameters)

	@property
	def gauss(self,
	) -> GaussRequest:
		from .gauss import GaussRequest
		return GaussRequest(self.request_adapter, self.path_parameters)

	@property
	def gcd(self,
	) -> GcdRequest:
		from .gcd import GcdRequest
		return GcdRequest(self.request_adapter, self.path_parameters)

	@property
	def geo_mean(self,
	) -> GeoMeanRequest:
		from .geo_mean import GeoMeanRequest
		return GeoMeanRequest(self.request_adapter, self.path_parameters)

	@property
	def ge_step(self,
	) -> GeStepRequest:
		from .ge_step import GeStepRequest
		return GeStepRequest(self.request_adapter, self.path_parameters)

	@property
	def har_mean(self,
	) -> HarMeanRequest:
		from .har_mean import HarMeanRequest
		return HarMeanRequest(self.request_adapter, self.path_parameters)

	@property
	def hex2_bin(self,
	) -> Hex2BinRequest:
		from .hex2_bin import Hex2BinRequest
		return Hex2BinRequest(self.request_adapter, self.path_parameters)

	@property
	def hex2_dec(self,
	) -> Hex2DecRequest:
		from .hex2_dec import Hex2DecRequest
		return Hex2DecRequest(self.request_adapter, self.path_parameters)

	@property
	def hex2_oct(self,
	) -> Hex2OctRequest:
		from .hex2_oct import Hex2OctRequest
		return Hex2OctRequest(self.request_adapter, self.path_parameters)

	@property
	def hlookup(self,
	) -> HlookupRequest:
		from .hlookup import HlookupRequest
		return HlookupRequest(self.request_adapter, self.path_parameters)

	@property
	def hour(self,
	) -> HourRequest:
		from .hour import HourRequest
		return HourRequest(self.request_adapter, self.path_parameters)

	@property
	def hyperlink(self,
	) -> HyperlinkRequest:
		from .hyperlink import HyperlinkRequest
		return HyperlinkRequest(self.request_adapter, self.path_parameters)

	@property
	def hyp_geom__dist(self,
	) -> HypGeom_DistRequest:
		from .hyp_geom__dist import HypGeom_DistRequest
		return HypGeom_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def if(self,
	) -> IfRequest:
		from .if import IfRequest
		return IfRequest(self.request_adapter, self.path_parameters)

	@property
	def im_abs(self,
	) -> ImAbsRequest:
		from .im_abs import ImAbsRequest
		return ImAbsRequest(self.request_adapter, self.path_parameters)

	@property
	def imaginary(self,
	) -> ImaginaryRequest:
		from .imaginary import ImaginaryRequest
		return ImaginaryRequest(self.request_adapter, self.path_parameters)

	@property
	def im_argument(self,
	) -> ImArgumentRequest:
		from .im_argument import ImArgumentRequest
		return ImArgumentRequest(self.request_adapter, self.path_parameters)

	@property
	def im_conjugate(self,
	) -> ImConjugateRequest:
		from .im_conjugate import ImConjugateRequest
		return ImConjugateRequest(self.request_adapter, self.path_parameters)

	@property
	def im_cos(self,
	) -> ImCosRequest:
		from .im_cos import ImCosRequest
		return ImCosRequest(self.request_adapter, self.path_parameters)

	@property
	def im_cosh(self,
	) -> ImCoshRequest:
		from .im_cosh import ImCoshRequest
		return ImCoshRequest(self.request_adapter, self.path_parameters)

	@property
	def im_cot(self,
	) -> ImCotRequest:
		from .im_cot import ImCotRequest
		return ImCotRequest(self.request_adapter, self.path_parameters)

	@property
	def im_csc(self,
	) -> ImCscRequest:
		from .im_csc import ImCscRequest
		return ImCscRequest(self.request_adapter, self.path_parameters)

	@property
	def im_csch(self,
	) -> ImCschRequest:
		from .im_csch import ImCschRequest
		return ImCschRequest(self.request_adapter, self.path_parameters)

	@property
	def im_div(self,
	) -> ImDivRequest:
		from .im_div import ImDivRequest
		return ImDivRequest(self.request_adapter, self.path_parameters)

	@property
	def im_exp(self,
	) -> ImExpRequest:
		from .im_exp import ImExpRequest
		return ImExpRequest(self.request_adapter, self.path_parameters)

	@property
	def im_ln(self,
	) -> ImLnRequest:
		from .im_ln import ImLnRequest
		return ImLnRequest(self.request_adapter, self.path_parameters)

	@property
	def im_log10(self,
	) -> ImLog10Request:
		from .im_log10 import ImLog10Request
		return ImLog10Request(self.request_adapter, self.path_parameters)

	@property
	def im_log2(self,
	) -> ImLog2Request:
		from .im_log2 import ImLog2Request
		return ImLog2Request(self.request_adapter, self.path_parameters)

	@property
	def im_power(self,
	) -> ImPowerRequest:
		from .im_power import ImPowerRequest
		return ImPowerRequest(self.request_adapter, self.path_parameters)

	@property
	def im_product(self,
	) -> ImProductRequest:
		from .im_product import ImProductRequest
		return ImProductRequest(self.request_adapter, self.path_parameters)

	@property
	def im_real(self,
	) -> ImRealRequest:
		from .im_real import ImRealRequest
		return ImRealRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sec(self,
	) -> ImSecRequest:
		from .im_sec import ImSecRequest
		return ImSecRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sech(self,
	) -> ImSechRequest:
		from .im_sech import ImSechRequest
		return ImSechRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sin(self,
	) -> ImSinRequest:
		from .im_sin import ImSinRequest
		return ImSinRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sinh(self,
	) -> ImSinhRequest:
		from .im_sinh import ImSinhRequest
		return ImSinhRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sqrt(self,
	) -> ImSqrtRequest:
		from .im_sqrt import ImSqrtRequest
		return ImSqrtRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sub(self,
	) -> ImSubRequest:
		from .im_sub import ImSubRequest
		return ImSubRequest(self.request_adapter, self.path_parameters)

	@property
	def im_sum(self,
	) -> ImSumRequest:
		from .im_sum import ImSumRequest
		return ImSumRequest(self.request_adapter, self.path_parameters)

	@property
	def im_tan(self,
	) -> ImTanRequest:
		from .im_tan import ImTanRequest
		return ImTanRequest(self.request_adapter, self.path_parameters)

	@property
	def int(self,
	) -> IntRequest:
		from .int import IntRequest
		return IntRequest(self.request_adapter, self.path_parameters)

	@property
	def int_rate(self,
	) -> IntRateRequest:
		from .int_rate import IntRateRequest
		return IntRateRequest(self.request_adapter, self.path_parameters)

	@property
	def ipmt(self,
	) -> IpmtRequest:
		from .ipmt import IpmtRequest
		return IpmtRequest(self.request_adapter, self.path_parameters)

	@property
	def irr(self,
	) -> IrrRequest:
		from .irr import IrrRequest
		return IrrRequest(self.request_adapter, self.path_parameters)

	@property
	def is_err(self,
	) -> IsErrRequest:
		from .is_err import IsErrRequest
		return IsErrRequest(self.request_adapter, self.path_parameters)

	@property
	def is_error(self,
	) -> IsErrorRequest:
		from .is_error import IsErrorRequest
		return IsErrorRequest(self.request_adapter, self.path_parameters)

	@property
	def is_even(self,
	) -> IsEvenRequest:
		from .is_even import IsEvenRequest
		return IsEvenRequest(self.request_adapter, self.path_parameters)

	@property
	def is_formula(self,
	) -> IsFormulaRequest:
		from .is_formula import IsFormulaRequest
		return IsFormulaRequest(self.request_adapter, self.path_parameters)

	@property
	def is_logical(self,
	) -> IsLogicalRequest:
		from .is_logical import IsLogicalRequest
		return IsLogicalRequest(self.request_adapter, self.path_parameters)

	@property
	def is_n_a(self,
	) -> IsNARequest:
		from .is_n_a import IsNARequest
		return IsNARequest(self.request_adapter, self.path_parameters)

	@property
	def is_non_text(self,
	) -> IsNonTextRequest:
		from .is_non_text import IsNonTextRequest
		return IsNonTextRequest(self.request_adapter, self.path_parameters)

	@property
	def is_number(self,
	) -> IsNumberRequest:
		from .is_number import IsNumberRequest
		return IsNumberRequest(self.request_adapter, self.path_parameters)

	@property
	def iso__ceiling(self,
	) -> Iso_CeilingRequest:
		from .iso__ceiling import Iso_CeilingRequest
		return Iso_CeilingRequest(self.request_adapter, self.path_parameters)

	@property
	def is_odd(self,
	) -> IsOddRequest:
		from .is_odd import IsOddRequest
		return IsOddRequest(self.request_adapter, self.path_parameters)

	@property
	def iso_week_num(self,
	) -> IsoWeekNumRequest:
		from .iso_week_num import IsoWeekNumRequest
		return IsoWeekNumRequest(self.request_adapter, self.path_parameters)

	@property
	def ispmt(self,
	) -> IspmtRequest:
		from .ispmt import IspmtRequest
		return IspmtRequest(self.request_adapter, self.path_parameters)

	@property
	def isref(self,
	) -> IsrefRequest:
		from .isref import IsrefRequest
		return IsrefRequest(self.request_adapter, self.path_parameters)

	@property
	def is_text(self,
	) -> IsTextRequest:
		from .is_text import IsTextRequest
		return IsTextRequest(self.request_adapter, self.path_parameters)

	@property
	def kurt(self,
	) -> KurtRequest:
		from .kurt import KurtRequest
		return KurtRequest(self.request_adapter, self.path_parameters)

	@property
	def large(self,
	) -> LargeRequest:
		from .large import LargeRequest
		return LargeRequest(self.request_adapter, self.path_parameters)

	@property
	def lcm(self,
	) -> LcmRequest:
		from .lcm import LcmRequest
		return LcmRequest(self.request_adapter, self.path_parameters)

	@property
	def left(self,
	) -> LeftRequest:
		from .left import LeftRequest
		return LeftRequest(self.request_adapter, self.path_parameters)

	@property
	def leftb(self,
	) -> LeftbRequest:
		from .leftb import LeftbRequest
		return LeftbRequest(self.request_adapter, self.path_parameters)

	@property
	def len(self,
	) -> LenRequest:
		from .len import LenRequest
		return LenRequest(self.request_adapter, self.path_parameters)

	@property
	def lenb(self,
	) -> LenbRequest:
		from .lenb import LenbRequest
		return LenbRequest(self.request_adapter, self.path_parameters)

	@property
	def ln(self,
	) -> LnRequest:
		from .ln import LnRequest
		return LnRequest(self.request_adapter, self.path_parameters)

	@property
	def log(self,
	) -> LogRequest:
		from .log import LogRequest
		return LogRequest(self.request_adapter, self.path_parameters)

	@property
	def log10(self,
	) -> Log10Request:
		from .log10 import Log10Request
		return Log10Request(self.request_adapter, self.path_parameters)

	@property
	def log_norm__dist(self,
	) -> LogNorm_DistRequest:
		from .log_norm__dist import LogNorm_DistRequest
		return LogNorm_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def log_norm__inv(self,
	) -> LogNorm_InvRequest:
		from .log_norm__inv import LogNorm_InvRequest
		return LogNorm_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def lookup(self,
	) -> LookupRequest:
		from .lookup import LookupRequest
		return LookupRequest(self.request_adapter, self.path_parameters)

	@property
	def lower(self,
	) -> LowerRequest:
		from .lower import LowerRequest
		return LowerRequest(self.request_adapter, self.path_parameters)

	@property
	def match(self,
	) -> MatchRequest:
		from .match import MatchRequest
		return MatchRequest(self.request_adapter, self.path_parameters)

	@property
	def max(self,
	) -> MaxRequest:
		from .max import MaxRequest
		return MaxRequest(self.request_adapter, self.path_parameters)

	@property
	def max_a(self,
	) -> MaxARequest:
		from .max_a import MaxARequest
		return MaxARequest(self.request_adapter, self.path_parameters)

	@property
	def mduration(self,
	) -> MdurationRequest:
		from .mduration import MdurationRequest
		return MdurationRequest(self.request_adapter, self.path_parameters)

	@property
	def median(self,
	) -> MedianRequest:
		from .median import MedianRequest
		return MedianRequest(self.request_adapter, self.path_parameters)

	@property
	def mid(self,
	) -> MidRequest:
		from .mid import MidRequest
		return MidRequest(self.request_adapter, self.path_parameters)

	@property
	def midb(self,
	) -> MidbRequest:
		from .midb import MidbRequest
		return MidbRequest(self.request_adapter, self.path_parameters)

	@property
	def min(self,
	) -> MinRequest:
		from .min import MinRequest
		return MinRequest(self.request_adapter, self.path_parameters)

	@property
	def min_a(self,
	) -> MinARequest:
		from .min_a import MinARequest
		return MinARequest(self.request_adapter, self.path_parameters)

	@property
	def minute(self,
	) -> MinuteRequest:
		from .minute import MinuteRequest
		return MinuteRequest(self.request_adapter, self.path_parameters)

	@property
	def mirr(self,
	) -> MirrRequest:
		from .mirr import MirrRequest
		return MirrRequest(self.request_adapter, self.path_parameters)

	@property
	def mod(self,
	) -> ModRequest:
		from .mod import ModRequest
		return ModRequest(self.request_adapter, self.path_parameters)

	@property
	def month(self,
	) -> MonthRequest:
		from .month import MonthRequest
		return MonthRequest(self.request_adapter, self.path_parameters)

	@property
	def mround(self,
	) -> MroundRequest:
		from .mround import MroundRequest
		return MroundRequest(self.request_adapter, self.path_parameters)

	@property
	def multi_nomial(self,
	) -> MultiNomialRequest:
		from .multi_nomial import MultiNomialRequest
		return MultiNomialRequest(self.request_adapter, self.path_parameters)

	@property
	def n(self,
	) -> NRequest:
		from .n import NRequest
		return NRequest(self.request_adapter, self.path_parameters)

	@property
	def na(self,
	) -> NaRequest:
		from .na import NaRequest
		return NaRequest(self.request_adapter, self.path_parameters)

	@property
	def neg_binom__dist(self,
	) -> NegBinom_DistRequest:
		from .neg_binom__dist import NegBinom_DistRequest
		return NegBinom_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def network_days(self,
	) -> NetworkDaysRequest:
		from .network_days import NetworkDaysRequest
		return NetworkDaysRequest(self.request_adapter, self.path_parameters)

	@property
	def network_days__intl(self,
	) -> NetworkDays_IntlRequest:
		from .network_days__intl import NetworkDays_IntlRequest
		return NetworkDays_IntlRequest(self.request_adapter, self.path_parameters)

	@property
	def nominal(self,
	) -> NominalRequest:
		from .nominal import NominalRequest
		return NominalRequest(self.request_adapter, self.path_parameters)

	@property
	def norm__dist(self,
	) -> Norm_DistRequest:
		from .norm__dist import Norm_DistRequest
		return Norm_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def norm__inv(self,
	) -> Norm_InvRequest:
		from .norm__inv import Norm_InvRequest
		return Norm_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def norm__s__dist(self,
	) -> Norm_S_DistRequest:
		from .norm__s__dist import Norm_S_DistRequest
		return Norm_S_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def norm__s__inv(self,
	) -> Norm_S_InvRequest:
		from .norm__s__inv import Norm_S_InvRequest
		return Norm_S_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def not(self,
	) -> NotRequest:
		from .not import NotRequest
		return NotRequest(self.request_adapter, self.path_parameters)

	@property
	def now(self,
	) -> NowRequest:
		from .now import NowRequest
		return NowRequest(self.request_adapter, self.path_parameters)

	@property
	def nper(self,
	) -> NperRequest:
		from .nper import NperRequest
		return NperRequest(self.request_adapter, self.path_parameters)

	@property
	def npv(self,
	) -> NpvRequest:
		from .npv import NpvRequest
		return NpvRequest(self.request_adapter, self.path_parameters)

	@property
	def number_value(self,
	) -> NumberValueRequest:
		from .number_value import NumberValueRequest
		return NumberValueRequest(self.request_adapter, self.path_parameters)

	@property
	def oct2_bin(self,
	) -> Oct2BinRequest:
		from .oct2_bin import Oct2BinRequest
		return Oct2BinRequest(self.request_adapter, self.path_parameters)

	@property
	def oct2_dec(self,
	) -> Oct2DecRequest:
		from .oct2_dec import Oct2DecRequest
		return Oct2DecRequest(self.request_adapter, self.path_parameters)

	@property
	def oct2_hex(self,
	) -> Oct2HexRequest:
		from .oct2_hex import Oct2HexRequest
		return Oct2HexRequest(self.request_adapter, self.path_parameters)

	@property
	def odd(self,
	) -> OddRequest:
		from .odd import OddRequest
		return OddRequest(self.request_adapter, self.path_parameters)

	@property
	def odd_f_price(self,
	) -> OddFPriceRequest:
		from .odd_f_price import OddFPriceRequest
		return OddFPriceRequest(self.request_adapter, self.path_parameters)

	@property
	def odd_f_yield(self,
	) -> OddFYieldRequest:
		from .odd_f_yield import OddFYieldRequest
		return OddFYieldRequest(self.request_adapter, self.path_parameters)

	@property
	def odd_l_price(self,
	) -> OddLPriceRequest:
		from .odd_l_price import OddLPriceRequest
		return OddLPriceRequest(self.request_adapter, self.path_parameters)

	@property
	def odd_l_yield(self,
	) -> OddLYieldRequest:
		from .odd_l_yield import OddLYieldRequest
		return OddLYieldRequest(self.request_adapter, self.path_parameters)

	@property
	def or(self,
	) -> OrRequest:
		from .or import OrRequest
		return OrRequest(self.request_adapter, self.path_parameters)

	@property
	def pduration(self,
	) -> PdurationRequest:
		from .pduration import PdurationRequest
		return PdurationRequest(self.request_adapter, self.path_parameters)

	@property
	def percentile__exc(self,
	) -> Percentile_ExcRequest:
		from .percentile__exc import Percentile_ExcRequest
		return Percentile_ExcRequest(self.request_adapter, self.path_parameters)

	@property
	def percentile__inc(self,
	) -> Percentile_IncRequest:
		from .percentile__inc import Percentile_IncRequest
		return Percentile_IncRequest(self.request_adapter, self.path_parameters)

	@property
	def percent_rank__exc(self,
	) -> PercentRank_ExcRequest:
		from .percent_rank__exc import PercentRank_ExcRequest
		return PercentRank_ExcRequest(self.request_adapter, self.path_parameters)

	@property
	def percent_rank__inc(self,
	) -> PercentRank_IncRequest:
		from .percent_rank__inc import PercentRank_IncRequest
		return PercentRank_IncRequest(self.request_adapter, self.path_parameters)

	@property
	def permut(self,
	) -> PermutRequest:
		from .permut import PermutRequest
		return PermutRequest(self.request_adapter, self.path_parameters)

	@property
	def permutationa(self,
	) -> PermutationaRequest:
		from .permutationa import PermutationaRequest
		return PermutationaRequest(self.request_adapter, self.path_parameters)

	@property
	def phi(self,
	) -> PhiRequest:
		from .phi import PhiRequest
		return PhiRequest(self.request_adapter, self.path_parameters)

	@property
	def pi(self,
	) -> PiRequest:
		from .pi import PiRequest
		return PiRequest(self.request_adapter, self.path_parameters)

	@property
	def pmt(self,
	) -> PmtRequest:
		from .pmt import PmtRequest
		return PmtRequest(self.request_adapter, self.path_parameters)

	@property
	def poisson__dist(self,
	) -> Poisson_DistRequest:
		from .poisson__dist import Poisson_DistRequest
		return Poisson_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def power(self,
	) -> PowerRequest:
		from .power import PowerRequest
		return PowerRequest(self.request_adapter, self.path_parameters)

	@property
	def ppmt(self,
	) -> PpmtRequest:
		from .ppmt import PpmtRequest
		return PpmtRequest(self.request_adapter, self.path_parameters)

	@property
	def price(self,
	) -> PriceRequest:
		from .price import PriceRequest
		return PriceRequest(self.request_adapter, self.path_parameters)

	@property
	def price_disc(self,
	) -> PriceDiscRequest:
		from .price_disc import PriceDiscRequest
		return PriceDiscRequest(self.request_adapter, self.path_parameters)

	@property
	def price_mat(self,
	) -> PriceMatRequest:
		from .price_mat import PriceMatRequest
		return PriceMatRequest(self.request_adapter, self.path_parameters)

	@property
	def product(self,
	) -> ProductRequest:
		from .product import ProductRequest
		return ProductRequest(self.request_adapter, self.path_parameters)

	@property
	def proper(self,
	) -> ProperRequest:
		from .proper import ProperRequest
		return ProperRequest(self.request_adapter, self.path_parameters)

	@property
	def pv(self,
	) -> PvRequest:
		from .pv import PvRequest
		return PvRequest(self.request_adapter, self.path_parameters)

	@property
	def quartile__exc(self,
	) -> Quartile_ExcRequest:
		from .quartile__exc import Quartile_ExcRequest
		return Quartile_ExcRequest(self.request_adapter, self.path_parameters)

	@property
	def quartile__inc(self,
	) -> Quartile_IncRequest:
		from .quartile__inc import Quartile_IncRequest
		return Quartile_IncRequest(self.request_adapter, self.path_parameters)

	@property
	def quotient(self,
	) -> QuotientRequest:
		from .quotient import QuotientRequest
		return QuotientRequest(self.request_adapter, self.path_parameters)

	@property
	def radians(self,
	) -> RadiansRequest:
		from .radians import RadiansRequest
		return RadiansRequest(self.request_adapter, self.path_parameters)

	@property
	def rand(self,
	) -> RandRequest:
		from .rand import RandRequest
		return RandRequest(self.request_adapter, self.path_parameters)

	@property
	def rand_between(self,
	) -> RandBetweenRequest:
		from .rand_between import RandBetweenRequest
		return RandBetweenRequest(self.request_adapter, self.path_parameters)

	@property
	def rank__avg(self,
	) -> Rank_AvgRequest:
		from .rank__avg import Rank_AvgRequest
		return Rank_AvgRequest(self.request_adapter, self.path_parameters)

	@property
	def rank__eq(self,
	) -> Rank_EqRequest:
		from .rank__eq import Rank_EqRequest
		return Rank_EqRequest(self.request_adapter, self.path_parameters)

	@property
	def rate(self,
	) -> RateRequest:
		from .rate import RateRequest
		return RateRequest(self.request_adapter, self.path_parameters)

	@property
	def received(self,
	) -> ReceivedRequest:
		from .received import ReceivedRequest
		return ReceivedRequest(self.request_adapter, self.path_parameters)

	@property
	def replace(self,
	) -> ReplaceRequest:
		from .replace import ReplaceRequest
		return ReplaceRequest(self.request_adapter, self.path_parameters)

	@property
	def replace_b(self,
	) -> ReplaceBRequest:
		from .replace_b import ReplaceBRequest
		return ReplaceBRequest(self.request_adapter, self.path_parameters)

	@property
	def rept(self,
	) -> ReptRequest:
		from .rept import ReptRequest
		return ReptRequest(self.request_adapter, self.path_parameters)

	@property
	def right(self,
	) -> RightRequest:
		from .right import RightRequest
		return RightRequest(self.request_adapter, self.path_parameters)

	@property
	def rightb(self,
	) -> RightbRequest:
		from .rightb import RightbRequest
		return RightbRequest(self.request_adapter, self.path_parameters)

	@property
	def roman(self,
	) -> RomanRequest:
		from .roman import RomanRequest
		return RomanRequest(self.request_adapter, self.path_parameters)

	@property
	def round(self,
	) -> RoundRequest:
		from .round import RoundRequest
		return RoundRequest(self.request_adapter, self.path_parameters)

	@property
	def round_down(self,
	) -> RoundDownRequest:
		from .round_down import RoundDownRequest
		return RoundDownRequest(self.request_adapter, self.path_parameters)

	@property
	def round_up(self,
	) -> RoundUpRequest:
		from .round_up import RoundUpRequest
		return RoundUpRequest(self.request_adapter, self.path_parameters)

	@property
	def rows(self,
	) -> RowsRequest:
		from .rows import RowsRequest
		return RowsRequest(self.request_adapter, self.path_parameters)

	@property
	def rri(self,
	) -> RriRequest:
		from .rri import RriRequest
		return RriRequest(self.request_adapter, self.path_parameters)

	@property
	def sec(self,
	) -> SecRequest:
		from .sec import SecRequest
		return SecRequest(self.request_adapter, self.path_parameters)

	@property
	def sech(self,
	) -> SechRequest:
		from .sech import SechRequest
		return SechRequest(self.request_adapter, self.path_parameters)

	@property
	def second(self,
	) -> SecondRequest:
		from .second import SecondRequest
		return SecondRequest(self.request_adapter, self.path_parameters)

	@property
	def series_sum(self,
	) -> SeriesSumRequest:
		from .series_sum import SeriesSumRequest
		return SeriesSumRequest(self.request_adapter, self.path_parameters)

	@property
	def sheet(self,
	) -> SheetRequest:
		from .sheet import SheetRequest
		return SheetRequest(self.request_adapter, self.path_parameters)

	@property
	def sheets(self,
	) -> SheetsRequest:
		from .sheets import SheetsRequest
		return SheetsRequest(self.request_adapter, self.path_parameters)

	@property
	def sign(self,
	) -> SignRequest:
		from .sign import SignRequest
		return SignRequest(self.request_adapter, self.path_parameters)

	@property
	def sin(self,
	) -> SinRequest:
		from .sin import SinRequest
		return SinRequest(self.request_adapter, self.path_parameters)

	@property
	def sinh(self,
	) -> SinhRequest:
		from .sinh import SinhRequest
		return SinhRequest(self.request_adapter, self.path_parameters)

	@property
	def skew(self,
	) -> SkewRequest:
		from .skew import SkewRequest
		return SkewRequest(self.request_adapter, self.path_parameters)

	@property
	def skew_p(self,
	) -> Skew_pRequest:
		from .skew_p import Skew_pRequest
		return Skew_pRequest(self.request_adapter, self.path_parameters)

	@property
	def sln(self,
	) -> SlnRequest:
		from .sln import SlnRequest
		return SlnRequest(self.request_adapter, self.path_parameters)

	@property
	def small(self,
	) -> SmallRequest:
		from .small import SmallRequest
		return SmallRequest(self.request_adapter, self.path_parameters)

	@property
	def sqrt(self,
	) -> SqrtRequest:
		from .sqrt import SqrtRequest
		return SqrtRequest(self.request_adapter, self.path_parameters)

	@property
	def sqrt_pi(self,
	) -> SqrtPiRequest:
		from .sqrt_pi import SqrtPiRequest
		return SqrtPiRequest(self.request_adapter, self.path_parameters)

	@property
	def standardize(self,
	) -> StandardizeRequest:
		from .standardize import StandardizeRequest
		return StandardizeRequest(self.request_adapter, self.path_parameters)

	@property
	def st_dev__p(self,
	) -> StDev_PRequest:
		from .st_dev__p import StDev_PRequest
		return StDev_PRequest(self.request_adapter, self.path_parameters)

	@property
	def st_dev__s(self,
	) -> StDev_SRequest:
		from .st_dev__s import StDev_SRequest
		return StDev_SRequest(self.request_adapter, self.path_parameters)

	@property
	def st_dev_a(self,
	) -> StDevARequest:
		from .st_dev_a import StDevARequest
		return StDevARequest(self.request_adapter, self.path_parameters)

	@property
	def st_dev_p_a(self,
	) -> StDevPARequest:
		from .st_dev_p_a import StDevPARequest
		return StDevPARequest(self.request_adapter, self.path_parameters)

	@property
	def substitute(self,
	) -> SubstituteRequest:
		from .substitute import SubstituteRequest
		return SubstituteRequest(self.request_adapter, self.path_parameters)

	@property
	def subtotal(self,
	) -> SubtotalRequest:
		from .subtotal import SubtotalRequest
		return SubtotalRequest(self.request_adapter, self.path_parameters)

	@property
	def sum(self,
	) -> SumRequest:
		from .sum import SumRequest
		return SumRequest(self.request_adapter, self.path_parameters)

	@property
	def sum_if(self,
	) -> SumIfRequest:
		from .sum_if import SumIfRequest
		return SumIfRequest(self.request_adapter, self.path_parameters)

	@property
	def sum_ifs(self,
	) -> SumIfsRequest:
		from .sum_ifs import SumIfsRequest
		return SumIfsRequest(self.request_adapter, self.path_parameters)

	@property
	def sum_sq(self,
	) -> SumSqRequest:
		from .sum_sq import SumSqRequest
		return SumSqRequest(self.request_adapter, self.path_parameters)

	@property
	def syd(self,
	) -> SydRequest:
		from .syd import SydRequest
		return SydRequest(self.request_adapter, self.path_parameters)

	@property
	def t(self,
	) -> TRequest:
		from .t import TRequest
		return TRequest(self.request_adapter, self.path_parameters)

	@property
	def t__dist(self,
	) -> T_DistRequest:
		from .t__dist import T_DistRequest
		return T_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def t__dist_2_t(self,
	) -> T_Dist_2TRequest:
		from .t__dist_2_t import T_Dist_2TRequest
		return T_Dist_2TRequest(self.request_adapter, self.path_parameters)

	@property
	def t__dist__r_t(self,
	) -> T_Dist_RTRequest:
		from .t__dist__r_t import T_Dist_RTRequest
		return T_Dist_RTRequest(self.request_adapter, self.path_parameters)

	@property
	def t__inv(self,
	) -> T_InvRequest:
		from .t__inv import T_InvRequest
		return T_InvRequest(self.request_adapter, self.path_parameters)

	@property
	def t__inv_2_t(self,
	) -> T_Inv_2TRequest:
		from .t__inv_2_t import T_Inv_2TRequest
		return T_Inv_2TRequest(self.request_adapter, self.path_parameters)

	@property
	def tan(self,
	) -> TanRequest:
		from .tan import TanRequest
		return TanRequest(self.request_adapter, self.path_parameters)

	@property
	def tanh(self,
	) -> TanhRequest:
		from .tanh import TanhRequest
		return TanhRequest(self.request_adapter, self.path_parameters)

	@property
	def tbill_eq(self,
	) -> TbillEqRequest:
		from .tbill_eq import TbillEqRequest
		return TbillEqRequest(self.request_adapter, self.path_parameters)

	@property
	def tbill_price(self,
	) -> TbillPriceRequest:
		from .tbill_price import TbillPriceRequest
		return TbillPriceRequest(self.request_adapter, self.path_parameters)

	@property
	def tbill_yield(self,
	) -> TbillYieldRequest:
		from .tbill_yield import TbillYieldRequest
		return TbillYieldRequest(self.request_adapter, self.path_parameters)

	@property
	def text(self,
	) -> TextRequest:
		from .text import TextRequest
		return TextRequest(self.request_adapter, self.path_parameters)

	@property
	def time(self,
	) -> TimeRequest:
		from .time import TimeRequest
		return TimeRequest(self.request_adapter, self.path_parameters)

	@property
	def timevalue(self,
	) -> TimevalueRequest:
		from .timevalue import TimevalueRequest
		return TimevalueRequest(self.request_adapter, self.path_parameters)

	@property
	def today(self,
	) -> TodayRequest:
		from .today import TodayRequest
		return TodayRequest(self.request_adapter, self.path_parameters)

	@property
	def trim(self,
	) -> TrimRequest:
		from .trim import TrimRequest
		return TrimRequest(self.request_adapter, self.path_parameters)

	@property
	def trim_mean(self,
	) -> TrimMeanRequest:
		from .trim_mean import TrimMeanRequest
		return TrimMeanRequest(self.request_adapter, self.path_parameters)

	@property
	def true(self,
	) -> TrueRequest:
		from .true import TrueRequest
		return TrueRequest(self.request_adapter, self.path_parameters)

	@property
	def trunc(self,
	) -> TruncRequest:
		from .trunc import TruncRequest
		return TruncRequest(self.request_adapter, self.path_parameters)

	@property
	def type(self,
	) -> TypeRequest:
		from .type import TypeRequest
		return TypeRequest(self.request_adapter, self.path_parameters)

	@property
	def unichar(self,
	) -> UnicharRequest:
		from .unichar import UnicharRequest
		return UnicharRequest(self.request_adapter, self.path_parameters)

	@property
	def unicode(self,
	) -> UnicodeRequest:
		from .unicode import UnicodeRequest
		return UnicodeRequest(self.request_adapter, self.path_parameters)

	@property
	def upper(self,
	) -> UpperRequest:
		from .upper import UpperRequest
		return UpperRequest(self.request_adapter, self.path_parameters)

	@property
	def usdollar(self,
	) -> UsdollarRequest:
		from .usdollar import UsdollarRequest
		return UsdollarRequest(self.request_adapter, self.path_parameters)

	@property
	def value(self,
	) -> ValueRequest:
		from .value import ValueRequest
		return ValueRequest(self.request_adapter, self.path_parameters)

	@property
	def var__p(self,
	) -> Var_PRequest:
		from .var__p import Var_PRequest
		return Var_PRequest(self.request_adapter, self.path_parameters)

	@property
	def var__s(self,
	) -> Var_SRequest:
		from .var__s import Var_SRequest
		return Var_SRequest(self.request_adapter, self.path_parameters)

	@property
	def var_a(self,
	) -> VarARequest:
		from .var_a import VarARequest
		return VarARequest(self.request_adapter, self.path_parameters)

	@property
	def var_p_a(self,
	) -> VarPARequest:
		from .var_p_a import VarPARequest
		return VarPARequest(self.request_adapter, self.path_parameters)

	@property
	def vdb(self,
	) -> VdbRequest:
		from .vdb import VdbRequest
		return VdbRequest(self.request_adapter, self.path_parameters)

	@property
	def vlookup(self,
	) -> VlookupRequest:
		from .vlookup import VlookupRequest
		return VlookupRequest(self.request_adapter, self.path_parameters)

	@property
	def weekday(self,
	) -> WeekdayRequest:
		from .weekday import WeekdayRequest
		return WeekdayRequest(self.request_adapter, self.path_parameters)

	@property
	def week_num(self,
	) -> WeekNumRequest:
		from .week_num import WeekNumRequest
		return WeekNumRequest(self.request_adapter, self.path_parameters)

	@property
	def weibull__dist(self,
	) -> Weibull_DistRequest:
		from .weibull__dist import Weibull_DistRequest
		return Weibull_DistRequest(self.request_adapter, self.path_parameters)

	@property
	def work_day(self,
	) -> WorkDayRequest:
		from .work_day import WorkDayRequest
		return WorkDayRequest(self.request_adapter, self.path_parameters)

	@property
	def work_day__intl(self,
	) -> WorkDay_IntlRequest:
		from .work_day__intl import WorkDay_IntlRequest
		return WorkDay_IntlRequest(self.request_adapter, self.path_parameters)

	@property
	def xirr(self,
	) -> XirrRequest:
		from .xirr import XirrRequest
		return XirrRequest(self.request_adapter, self.path_parameters)

	@property
	def xnpv(self,
	) -> XnpvRequest:
		from .xnpv import XnpvRequest
		return XnpvRequest(self.request_adapter, self.path_parameters)

	@property
	def xor(self,
	) -> XorRequest:
		from .xor import XorRequest
		return XorRequest(self.request_adapter, self.path_parameters)

	@property
	def year(self,
	) -> YearRequest:
		from .year import YearRequest
		return YearRequest(self.request_adapter, self.path_parameters)

	@property
	def year_frac(self,
	) -> YearFracRequest:
		from .year_frac import YearFracRequest
		return YearFracRequest(self.request_adapter, self.path_parameters)

	@property
	def yield(self,
	) -> YieldRequest:
		from .yield import YieldRequest
		return YieldRequest(self.request_adapter, self.path_parameters)

	@property
	def yield_disc(self,
	) -> YieldDiscRequest:
		from .yield_disc import YieldDiscRequest
		return YieldDiscRequest(self.request_adapter, self.path_parameters)

	@property
	def yield_mat(self,
	) -> YieldMatRequest:
		from .yield_mat import YieldMatRequest
		return YieldMatRequest(self.request_adapter, self.path_parameters)

	@property
	def z__test(self,
	) -> Z_TestRequest:
		from .z__test import Z_TestRequest
		return Z_TestRequest(self.request_adapter, self.path_parameters)

