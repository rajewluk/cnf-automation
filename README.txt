Apache Helm package Demo with ONAP, onap-sdk and dedicated automation scripts. Directory structure:

/templates/           #Base directory containing Apache resources
    |- /base_native   #Directory containing base payload of VSP package in Helm VSP, doesn't need further proceeding
    |- /helm          #Directory containing helm charts that need to be packaged and attached to VSP package
    \- /cba           #Directory containing CBA content to be included to csar package.
/automation/          #Directory with automation scripts. For more details read README file inside.

Note: Makefile script generates VSP package in native Helm VSP format where helm packages are standalone.
