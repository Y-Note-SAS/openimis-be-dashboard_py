import graphene
from graphene import ObjectType, String, Int, Float, List, Field
from graphene_django import DjangoObjectType

# Geospatial Types
class RegionSummaryType(ObjectType):
    region_name = String()
    total_claimed_amount = String()
    claim_count = Int()

class ProviderNetworkDetailType(ObjectType):
    facility_name = String()
    location_name = String()
    district_name = String()
    province_name = String()

class GeospatialAnalyticsGQLType(ObjectType):
    claim_summary_by_province = List(RegionSummaryType)
    provider_network_details = List(ProviderNetworkDetailType)


# Epidemiological Types
class IcdSummaryType(ObjectType):
    icd_name = String()
    claim_count = Int()
    total_claimed_amount = Float()

class DiseaseTrendPointType(ObjectType):
    month = String()
    claim_count = Int()

class EpidemiologicalAnalyticsGQLType(ObjectType):
    top_claimed_diseases_by_volume = List(IcdSummaryType)
    top_claimed_diseases_by_cost = List(IcdSummaryType)
    overall_claim_trend = List(DiseaseTrendPointType)


# Customer Journey Types
class ClaimLifecycleFunnelType(ObjectType):
    stage_name = String()
    claim_count = Int()

class RejectionReasonSummaryType(ObjectType):
    rejection_reason_code = String()
    claim_count = Int()

class ClaimPaymentTimeType(ObjectType):
    time_bracket = String()
    claim_count = Int()

class CustomerJourneyAnalyticsGQLType(ObjectType):
    claim_lifecycle_funnel = List(ClaimLifecycleFunnelType)
    rejection_reason_summary = List(RejectionReasonSummaryType)
    claims_pending_feedback_count = Int()
    claim_payment_times = List(ClaimPaymentTimeType)


# Operational Types
class ClaimTurnaroundType(ObjectType):
    category_name = String()
    average_turnaround_days = Float()

class AdjusterPerformanceType(ObjectType):
    adjuster_name = String()
    claims_processed_count = Int()
    average_adjustment_amount = Float()
    approval_to_claim_ratio = Float()

class HealthFacilityQualityType(ObjectType):
    health_facility_name = String()
    total_claims_submitted = Int()
    rejection_rate_percentage = Float()
    average_claim_value = Float()

class OperationalAnalyticsGQLType(ObjectType):
    turnaround_by_facility = List(ClaimTurnaroundType)
    adjuster_performance = List(AdjusterPerformanceType)
    facility_quality_overview = List(HealthFacilityQualityType)


# Social Protection Types
class ProductClaimSummaryType(ObjectType):
    product_name = String()
    total_claimed_amount = Float()
    total_claims_count = Int()

class SubProductClaimSummaryType(ObjectType):
    sub_product_name = String()
    total_claimed_amount = Float()
    total_claims_count = Int()

class ProductInsureeCountType(ObjectType):
    product_name = String()
    unique_insuree_count = Int()

class SocialProtectionAnalyticsGQLType(ObjectType):
    claims_by_product = List(ProductClaimSummaryType)
    claims_by_sub_product = List(SubProductClaimSummaryType)
    insurees_by_product = List(ProductInsureeCountType)


# General Analytics Types
class TopClaimType(ObjectType):
    claim_id = Int()
    claim_code = String()
    claimed_amount = Float()
    health_facility_name = String()

class HealthFacilityClaimSummaryType(ObjectType):
    health_facility_name = String()
    total_claimed_amount = Float()

class AnalyticsGQLType(ObjectType):
    top_recommended_claims = List(TopClaimType)
    top_highest_claimed_claims = List(TopClaimType)
    top_valuated_claims = List(TopClaimType)
    total_claimed_by_health_facility = List(HealthFacilityClaimSummaryType)


# Dashboard Types
class DashboardGQLType(ObjectType):
    # Claim Processing Status
    claims_entered = Int()
    claims_checked = Int()
    claims_processed = Int()
    claims_valuated = Int()
    claims_rejected = Int()
    claims_pending = Int()
    
    # Healthcare Service Types
    inpatient_claims = Int()
    outpatient_claims = Int()
    emergency_visits = Int()
    routine_visits = Int()
    referral_claims = Int()
    
    # Health Facility Levels
    primary_care_claims = Int()
    secondary_care_claims = Int()
    tertiary_care_claims = Int()
    specialized_care_claims = Int()
    
    # Financial Metrics
    total_claimed_amount = Float()
    total_approved_amount = Float()
    average_claim_value = Float()
    high_value_claims = Int()
    
    # Quality Indicators
    claims_with_feedback = Int()
    claims_requiring_review = Int()
    claims_with_attachments = Int()
    pre_authorized_claims = Int()
    
    # Time-based Metrics
    claims_this_month = Int()
    claims_last_month = Int()
    processing_efficiency_rate = Float()

