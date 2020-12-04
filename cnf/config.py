class Config:
    #### REGION DETAILS ####
    NATIVE = True
    COMPLEX_ID = "complex"
    CLOUD_OWNER = "k8sCloudOwner"
    CLOUD_REGION = "k8s-region-1"
    AVAILABILITY_ZONE_NAME = "k8s-availability-zone"
    HYPERVISOR_TYPE = "k8s"
    TENANT_NAME = "k8s-tenant-1"
    K8S_NAMESPACE = "vfirewall"
    CUSTOMER_RESOURCE_DEFINITIONS = ["crds/crd1",
                                     "crds/crd2"]

    CLUSTER_KUBECONFIG_PATH = "artifacts/cluster_kubeconfig"
    ONAP_KUBECONFIG_PATH = "artifacts/onap_kubeconfig"

    #### SERVICE DETAILS ####
    GLOBAL_CUSTOMER_ID = "Michal_customer"
    VSPFILE = "vsp/native_vfw_k8s_demo.zip"
    VENDOR = "Michal_vendor"
    SERVICENAME = "native_vfw_k8s_demo_CNF_fixed"
    VSPNAME = "VSP_" + SERVICENAME
    VFNAME = "VF_" + SERVICENAME
    SERVICE_INSTANCE_NAME = "INSTANCE_" + SERVICENAME
    SDNC_ARTIFACT_NAME = "vnf"
    VF_MODULE_PREFIX = ""
    if NATIVE:
        VF_MODULE_PREFIX = "helm_"

    VF_MODULE_LIST = {VF_MODULE_PREFIX + "base_template":
                          {"name": VF_MODULE_PREFIX + "base_template",
                           "k8s-rb-profile-name": "vfw-cnf-cds-base-profile",
                           "k8s-rb-profile-namespace": K8S_NAMESPACE},
                      VF_MODULE_PREFIX + "vfw":
                          {"name": VF_MODULE_PREFIX + "vfw",
                           "k8s-rb-profile-name": "vfw-cnf-cds-base-profile",
                           "k8s-rb-profile-namespace": K8S_NAMESPACE},
                      VF_MODULE_PREFIX + "vpkg":
                          {"name": VF_MODULE_PREFIX + "vpkg",
                           "k8s-rb-profile-name": "vfw-cnf-cds-base-profile",
                           "k8s-rb-profile-namespace": K8S_NAMESPACE},
                      VF_MODULE_PREFIX + "vsn":
                          {"name": VF_MODULE_PREFIX + "vsn",
                           "k8s-rb-profile-name": "vfw-cnf-cds-base-profile",
                           "k8s-rb-profile-namespace": K8S_NAMESPACE}}

    ######## DEFAULT VALUES ########
    OWNING_ENTITY = "OE-Demonstration"
    PROJECT = "Project-Demonstration"
    PLATFORM = "test"
    LINE_OF_BUSINESS = "LOB-Demonstration"

