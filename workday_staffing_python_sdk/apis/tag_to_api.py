import typing_extensions

from workday_staffing_python_sdk.apis.tags import TagValues
from workday_staffing_python_sdk.apis.tags.prompt_values_api import PromptValuesApi
from workday_staffing_python_sdk.apis.tags.job_changes_api import JobChangesApi
from workday_staffing_python_sdk.apis.tags.workers_api import WorkersApi
from workday_staffing_python_sdk.apis.tags.organization_assignment_changes_api import OrganizationAssignmentChangesApi
from workday_staffing_python_sdk.apis.tags.supervisory_organizations_api import SupervisoryOrganizationsApi
from workday_staffing_python_sdk.apis.tags.jobs_api import JobsApi
from workday_staffing_python_sdk.apis.tags.job_families_api import JobFamiliesApi
from workday_staffing_python_sdk.apis.tags.job_profiles_api import JobProfilesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.JOB_CHANGES: JobChangesApi,
        TagValues.WORKERS: WorkersApi,
        TagValues.ORGANIZATION_ASSIGNMENT_CHANGES: OrganizationAssignmentChangesApi,
        TagValues.SUPERVISORY_ORGANIZATIONS: SupervisoryOrganizationsApi,
        TagValues.JOBS: JobsApi,
        TagValues.JOB_FAMILIES: JobFamiliesApi,
        TagValues.JOB_PROFILES: JobProfilesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.JOB_CHANGES: JobChangesApi,
        TagValues.WORKERS: WorkersApi,
        TagValues.ORGANIZATION_ASSIGNMENT_CHANGES: OrganizationAssignmentChangesApi,
        TagValues.SUPERVISORY_ORGANIZATIONS: SupervisoryOrganizationsApi,
        TagValues.JOBS: JobsApi,
        TagValues.JOB_FAMILIES: JobFamiliesApi,
        TagValues.JOB_PROFILES: JobProfilesApi,
    }
)
