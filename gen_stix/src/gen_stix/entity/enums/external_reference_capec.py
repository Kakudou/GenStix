"""This enum will contains all the valid CAPEC-ID/name"""

from enum import Enum


class ExternalReferenceCapec(Enum):
    ACCESSING_FUNCTIONALITY_NOT_PROPERLY_CONSTRAINED_BY_ACLS = (
        1,
        "Accessing Functionality Not Properly Constrained by ACLs",
    )
    INDUCING_ACCOUNT_LOCKOUT = (2, "Inducing Account Lockout")
    USING_LEADING_GHOST_CHARACTER_SEQUENCES_TO_BYPASS_INPUT_FILTERS = (
        3,
        "Using Leading 'Ghost' Character Sequences to Bypass Input Filters",
    )
    USING_ALTERNATIVE_IP_ADDRESS_ENCODINGS = (
        4,
        "Using Alternative IP Address Encodings",
    )
    ARGUMENT_INJECTION = (6, "Argument Injection")
    BLIND_SQL_INJECTION = (7, "Blind SQL Injection")
    BUFFER_OVERFLOW_IN_AN_API_CALL = (8, "Buffer Overflow in an API Call")
    BUFFER_OVERFLOW_IN_LOCAL_COMMANDLINE_UTILITIES = (
        9,
        "Buffer Overflow in Local Command-Line Utilities",
    )
    BUFFER_OVERFLOW_VIA_ENVIRONMENT_VARIABLES = (
        10,
        "Buffer Overflow via Environment Variables",
    )
    CAUSE_WEB_SERVER_MISCLASSIFICATION = (
        11,
        "Cause Web Server Misclassification",
    )
    CHOOSING_MESSAGE_IDENTIFIER = (12, "Choosing Message Identifier")
    SUBVERTING_ENVIRONMENT_VARIABLE_VALUES = (
        13,
        "Subverting Environment Variable Values",
    )
    CLIENTSIDE_INJECTIONINDUCED_BUFFER_OVERFLOW = (
        14,
        "Client-side Injection-induced Buffer Overflow",
    )
    COMMAND_DELIMITERS = (15, "Command Delimiters")
    DICTIONARYBASED_PASSWORD_ATTACK = (16, "Dictionary-based Password Attack")
    USING_MALICIOUS_FILES = (17, "Using Malicious Files")
    XSS_TARGETING_NONSCRIPT_ELEMENTS = (
        18,
        "XSS Targeting Non-Script Elements",
    )
    EMBEDDING_SCRIPTS_WITHIN_SCRIPTS = (19, "Embedding Scripts within Scripts")
    ENCRYPTION_BRUTE_FORCING = (20, "Encryption Brute Forcing")
    EXPLOITATION_OF_TRUSTED_IDENTIFIERS = (
        21,
        "Exploitation of Trusted Identifiers",
    )
    EXPLOITING_TRUST_IN_CLIENT = (22, "Exploiting Trust in Client")
    FILE_CONTENT_INJECTION = (23, "File Content Injection")
    FILTER_FAILURE_THROUGH_BUFFER_OVERFLOW = (
        24,
        "Filter Failure through Buffer Overflow",
    )
    FORCED_DEADLOCK = (25, "Forced Deadlock")
    LEVERAGING_RACE_CONDITIONS = (26, "Leveraging Race Conditions")
    LEVERAGING_RACE_CONDITIONS_VIA_SYMBOLIC_LINKS = (
        27,
        "Leveraging Race Conditions via Symbolic Links",
    )
    FUZZING = (28, "Fuzzing")
    LEVERAGING_TIMEOFCHECK_AND_TIMEOFUSE_TOCTOU_RACE_CONDITIONS = (
        29,
        "Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions",
    )
    HIJACKING_A_PRIVILEGED_THREAD_OF_EXECUTION = (
        30,
        "Hijacking a Privileged Thread of Execution",
    )
    ACCESSINGINTERCEPTINGMODIFYING_HTTP_COOKIES = (
        31,
        "Accessing/Intercepting/Modifying HTTP Cookies",
    )
    XSS_THROUGH_HTTP_QUERY_STRINGS = (32, "XSS Through HTTP Query Strings")
    HTTP_REQUEST_SMUGGLING = (33, "HTTP Request Smuggling")
    HTTP_RESPONSE_SPLITTING = (34, "HTTP Response Splitting")
    LEVERAGE_EXECUTABLE_CODE_IN_NONEXECUTABLE_FILES = (
        35,
        "Leverage Executable Code in Non-Executable Files",
    )
    USING_UNPUBLISHED_INTERFACES_OR_FUNCTIONALITY = (
        36,
        "Using Unpublished Interfaces or Functionality",
    )
    RETRIEVE_EMBEDDED_SENSITIVE_DATA = (37, "Retrieve Embedded Sensitive Data")
    LEVERAGINGMANIPULATING_CONFIGURATION_FILE_SEARCH_PATHS = (
        38,
        "Leveraging/Manipulating Configuration File Search Paths",
    )
    MANIPULATING_OPAQUE_CLIENTBASED_DATA_TOKENS = (
        39,
        "Manipulating Opaque Client-based Data Tokens",
    )
    MANIPULATING_WRITEABLE_TERMINAL_DEVICES = (
        40,
        "Manipulating Writeable Terminal Devices",
    )
    USING_METACHARACTERS_IN_EMAIL_HEADERS_TO_INJECT_MALICIOUS_PAYLOADS = (
        41,
        "Using Meta-characters in E-mail Headers to Inject Malicious Payloads",
    )
    MIME_CONVERSION = (42, "MIME Conversion")
    EXPLOITING_MULTIPLE_INPUT_INTERPRETATION_LAYERS = (
        43,
        "Exploiting Multiple Input Interpretation Layers",
    )
    OVERFLOW_BINARY_RESOURCE_FILE = (44, "Overflow Binary Resource File")
    BUFFER_OVERFLOW_VIA_SYMBOLIC_LINKS = (
        45,
        "Buffer Overflow via Symbolic Links",
    )
    OVERFLOW_VARIABLES_AND_TAGS = (46, "Overflow Variables and Tags")
    BUFFER_OVERFLOW_VIA_PARAMETER_EXPANSION = (
        47,
        "Buffer Overflow via Parameter Expansion",
    )
    PASSING_LOCAL_FILENAMES_TO_FUNCTIONS_THAT_EXPECT_A_URL = (
        48,
        "Passing Local Filenames to Functions That Expect a URL",
    )
    PASSWORD_BRUTE_FORCING = (49, "Password Brute Forcing")
    PASSWORD_RECOVERY_EXPLOITATION = (50, "Password Recovery Exploitation")
    POISON_WEB_SERVICE_REGISTRY = (51, "Poison Web Service Registry")
    EMBEDDING_NULL_BYTES = (52, "Embedding NULL Bytes")
    POSTFIX_NULL_TERMINATE_AND_BACKSLASH = (
        53,
        "Postfix, Null Terminate, and Backslash",
    )
    QUERY_SYSTEM_FOR_INFORMATION = (54, "Query System for Information")
    RAINBOW_TABLE_PASSWORD_CRACKING = (55, "Rainbow Table Password Cracking")
    UTILIZING_RESTS_TRUST_IN_THE_SYSTEM_RESOURCE_TO_OBTAIN_SENSITIVE_DATA = (
        57,
        "Utilizing REST's Trust in the System Resource to Obtain Sensitive Data",
    )
    RESTFUL_PRIVILEGE_ELEVATION = (58, "Restful Privilege Elevation")
    SESSION_CREDENTIAL_FALSIFICATION_THROUGH_PREDICTION = (
        59,
        "Session Credential Falsification through Prediction",
    )
    REUSING_SESSION_IDS_AKA_SESSION_REPLAY = (
        60,
        "Reusing Session IDs (aka Session Replay)",
    )
    SESSION_FIXATION = (61, "Session Fixation")
    CROSS_SITE_REQUEST_FORGERY = (62, "Cross Site Request Forgery")
    CROSSSITE_SCRIPTING_XSS = (63, "Cross-Site Scripting (XSS)")
    USING_SLASHES_AND_URL_ENCODING_COMBINED_TO_BYPASS_VALIDATION_LOGIC = (
        64,
        "Using Slashes and URL Encoding Combined to Bypass Validation Logic",
    )
    SNIFF_APPLICATION_CODE = (65, "Sniff Application Code")
    SQL_INJECTION = (66, "SQL Injection")
    STRING_FORMAT_OVERFLOW_IN_SYSLOG = (
        67,
        "String Format Overflow in syslog()",
    )
    SUBVERT_CODESIGNING_FACILITIES = (68, "Subvert Code-signing Facilities")
    TARGET_PROGRAMS_WITH_ELEVATED_PRIVILEGES = (
        69,
        "Target Programs with Elevated Privileges",
    )
    TRY_COMMON_OR_DEFAULT_USERNAMES_AND_PASSWORDS = (
        70,
        "Try Common or Default Usernames and Passwords",
    )
    USING_UNICODE_ENCODING_TO_BYPASS_VALIDATION_LOGIC = (
        71,
        "Using Unicode Encoding to Bypass Validation Logic",
    )
    URL_ENCODING = (72, "URL Encoding")
    USERCONTROLLED_FILENAME = (73, "User-Controlled Filename")
    MANIPULATING_STATE = (74, "Manipulating State")
    MANIPULATING_WRITEABLE_CONFIGURATION_FILES = (
        75,
        "Manipulating Writeable Configuration Files",
    )
    MANIPULATING_WEB_INPUT_TO_FILE_SYSTEM_CALLS = (
        76,
        "Manipulating Web Input to File System Calls",
    )
    MANIPULATING_USERCONTROLLED_VARIABLES = (
        77,
        "Manipulating User-Controlled Variables",
    )
    USING_ESCAPED_SLASHES_IN_ALTERNATE_ENCODING = (
        78,
        "Using Escaped Slashes in Alternate Encoding",
    )
    USING_SLASHES_IN_ALTERNATE_ENCODING = (
        79,
        "Using Slashes in Alternate Encoding",
    )
    USING_UTF_ENCODING_TO_BYPASS_VALIDATION_LOGIC = (
        80,
        "Using UTF-8 Encoding to Bypass Validation Logic",
    )
    WEB_SERVER_LOGS_TAMPERING = (81, "Web Server Logs Tampering")
    XPATH_INJECTION = (83, "XPath Injection")
    XQUERY_INJECTION = (84, "XQuery Injection")
    AJAX_FOOTPRINTING = (85, "AJAX Footprinting")
    XSS_THROUGH_HTTP_HEADERS = (86, "XSS Through HTTP Headers")
    FORCEFUL_BROWSING = (87, "Forceful Browsing")
    OS_COMMAND_INJECTION = (88, "OS Command Injection")
    PHARMING = (89, "Pharming")
    REFLECTION_ATTACK_IN_AUTHENTICATION_PROTOCOL = (
        90,
        "Reflection Attack in Authentication Protocol",
    )
    FORCED_INTEGER_OVERFLOW = (92, "Forced Integer Overflow")
    LOG_INJECTIONTAMPERINGFORGING = (93, "Log Injection-Tampering-Forging")
    ADVERSARY_IN_THE_MIDDLE_AITM = (94, "Adversary in the Middle (AiTM)")
    WSDL_SCANNING = (95, "WSDL Scanning")
    BLOCK_ACCESS_TO_LIBRARIES = (96, "Block Access to Libraries")
    CRYPTANALYSIS = (97, "Cryptanalysis")
    PHISHING = (98, "Phishing")
    OVERFLOW_BUFFERS = (100, "Overflow Buffers")
    SERVER_SIDE_INCLUDE_SSI_INJECTION = (
        101,
        "Server Side Include (SSI) Injection",
    )
    SESSION_SIDEJACKING = (102, "Session Sidejacking")
    CLICKJACKING = (103, "Clickjacking")
    CROSS_ZONE_SCRIPTING = (104, "Cross Zone Scripting")
    HTTP_REQUEST_SPLITTING = (105, "HTTP Request Splitting")
    CROSS_SITE_TRACING = (107, "Cross Site Tracing")
    COMMAND_LINE_EXECUTION_THROUGH_SQL_INJECTION = (
        108,
        "Command Line Execution through SQL Injection",
    )
    OBJECT_RELATIONAL_MAPPING_INJECTION = (
        109,
        "Object Relational Mapping Injection",
    )
    SQL_INJECTION_THROUGH_SOAP_PARAMETER_TAMPERING = (
        110,
        "SQL Injection through SOAP Parameter Tampering",
    )
    JSON_HIJACKING_AKA_JAVASCRIPT_HIJACKING = (
        111,
        "JSON Hijacking (aka JavaScript Hijacking)",
    )
    BRUTE_FORCE = (112, "Brute Force")
    INTERFACE_MANIPULATION = (113, "Interface Manipulation")
    AUTHENTICATION_ABUSE = (114, "Authentication Abuse")
    AUTHENTICATION_BYPASS = (115, "Authentication Bypass")
    EXCAVATION = (116, "Excavation")
    INTERCEPTION = (117, "Interception")
    DOUBLE_ENCODING = (120, "Double Encoding")
    EXPLOIT_NONPRODUCTION_INTERFACES = (
        121,
        "Exploit Non-Production Interfaces",
    )
    PRIVILEGE_ABUSE = (122, "Privilege Abuse")
    BUFFER_MANIPULATION = (123, "Buffer Manipulation")
    SHARED_RESOURCE_MANIPULATION = (124, "Shared Resource Manipulation")
    FLOODING = (125, "Flooding")
    PATH_TRAVERSAL = (126, "Path Traversal")
    DIRECTORY_INDEXING = (127, "Directory Indexing")
    INTEGER_ATTACKS = (128, "Integer Attacks")
    POINTER_MANIPULATION = (129, "Pointer Manipulation")
    EXCESSIVE_ALLOCATION = (130, "Excessive Allocation")
    RESOURCE_LEAK_EXPOSURE = (131, "Resource Leak Exposure")
    SYMLINK_ATTACK = (132, "Symlink Attack")
    TRY_ALL_COMMON_SWITCHES = (133, "Try All Common Switches")
    EMAIL_INJECTION = (134, "Email Injection")
    FORMAT_STRING_INJECTION = (135, "Format String Injection")
    LDAP_INJECTION = (136, "LDAP Injection")
    PARAMETER_INJECTION = (137, "Parameter Injection")
    REFLECTION_INJECTION = (138, "Reflection Injection")
    RELATIVE_PATH_TRAVERSAL = (139, "Relative Path Traversal")
    BYPASSING_OF_INTERMEDIATE_FORMS_IN_MULTIPLEFORM_SETS = (
        140,
        "Bypassing of Intermediate Forms in Multiple-Form Sets",
    )
    CACHE_POISONING = (141, "Cache Poisoning")
    DNS_CACHE_POISONING = (142, "DNS Cache Poisoning")
    DETECT_UNPUBLICIZED_WEB_PAGES = (143, "Detect Unpublicized Web Pages")
    DETECT_UNPUBLICIZED_WEB_SERVICES = (
        144,
        "Detect Unpublicized Web Services",
    )
    CHECKSUM_SPOOFING = (145, "Checksum Spoofing")
    XML_SCHEMA_POISONING = (146, "XML Schema Poisoning")
    XML_PING_OF_THE_DEATH = (147, "XML Ping of the Death")
    CONTENT_SPOOFING = (148, "Content Spoofing")
    EXPLORE_FOR_PREDICTABLE_TEMPORARY_FILE_NAMES = (
        149,
        "Explore for Predictable Temporary File Names",
    )
    COLLECT_DATA_FROM_COMMON_RESOURCE_LOCATIONS = (
        150,
        "Collect Data from Common Resource Locations",
    )
    IDENTITY_SPOOFING = (151, "Identity Spoofing")
    INPUT_DATA_MANIPULATION = (153, "Input Data Manipulation")
    RESOURCE_LOCATION_SPOOFING = (154, "Resource Location Spoofing")
    SCREEN_TEMPORARY_FILES_FOR_SENSITIVE_INFORMATION = (
        155,
        "Screen Temporary Files for Sensitive Information",
    )
    SNIFFING_ATTACKS = (157, "Sniffing Attacks")
    SNIFFING_NETWORK_TRAFFIC = (158, "Sniffing Network Traffic")
    REDIRECT_ACCESS_TO_LIBRARIES = (159, "Redirect Access to Libraries")
    EXPLOIT_SCRIPTBASED_APIS = (160, "Exploit Script-Based APIs")
    INFRASTRUCTURE_MANIPULATION = (161, "Infrastructure Manipulation")
    MANIPULATING_HIDDEN_FIELDS = (162, "Manipulating Hidden Fields")
    SPEAR_PHISHING = (163, "Spear Phishing")
    MOBILE_PHISHING = (164, "Mobile Phishing")
    FILE_MANIPULATION = (165, "File Manipulation")
    FORCE_THE_SYSTEM_TO_RESET_VALUES = (
        166,
        "Force the System to Reset Values",
    )
    WHITE_BOX_REVERSE_ENGINEERING = (167, "White Box Reverse Engineering")
    WINDOWS_DATA_ALTERNATE_DATA_STREAM = (
        168,
        "Windows ::DATA Alternate Data Stream",
    )
    FOOTPRINTING = (169, "Footprinting")
    WEB_APPLICATION_FINGERPRINTING = (170, "Web Application Fingerprinting")
    ACTION_SPOOFING = (173, "Action Spoofing")
    FLASH_PARAMETER_INJECTION = (174, "Flash Parameter Injection")
    CODE_INCLUSION = (175, "Code Inclusion")
    CONFIGURATIONENVIRONMENT_MANIPULATION = (
        176,
        "Configuration/Environment Manipulation",
    )
    CREATE_FILES_WITH_THE_SAME_NAME_AS_FILES_PROTECTED_WITH_A_HIGHER_CLASSIFICATION = (
        177,
        "Create files with the same name as files protected with a higher classification",
    )
    CROSSSITE_FLASHING = (178, "Cross-Site Flashing")
    CALLING_MICROSERVICES_DIRECTLY = (179, "Calling Micro-Services Directly")
    EXPLOITING_INCORRECTLY_CONFIGURED_ACCESS_CONTROL_SECURITY_LEVELS = (
        180,
        "Exploiting Incorrectly Configured Access Control Security Levels",
    )
    FLASH_FILE_OVERLAY = (181, "Flash File Overlay")
    FLASH_INJECTION = (182, "Flash Injection")
    IMAPSMTP_COMMAND_INJECTION = (183, "IMAP/SMTP Command Injection")
    SOFTWARE_INTEGRITY_ATTACK = (184, "Software Integrity Attack")
    MALICIOUS_SOFTWARE_DOWNLOAD = (185, "Malicious Software Download")
    MALICIOUS_SOFTWARE_UPDATE = (186, "Malicious Software Update")
    MALICIOUS_AUTOMATED_SOFTWARE_UPDATE_VIA_REDIRECTION = (
        187,
        "Malicious Automated Software Update via Redirection",
    )
    REVERSE_ENGINEERING = (188, "Reverse Engineering")
    BLACK_BOX_REVERSE_ENGINEERING = (189, "Black Box Reverse Engineering")
    REVERSE_ENGINEER_AN_EXECUTABLE_TO_EXPOSE_ASSUMED_HIDDEN_FUNCTIONALITY = (
        190,
        "Reverse Engineer an Executable to Expose Assumed Hidden Functionality",
    )
    READ_SENSITIVE_CONSTANTS_WITHIN_AN_EXECUTABLE = (
        191,
        "Read Sensitive Constants Within an Executable",
    )
    PROTOCOL_ANALYSIS = (192, "Protocol Analysis")
    PHP_REMOTE_FILE_INCLUSION = (193, "PHP Remote File Inclusion")
    FAKE_THE_SOURCE_OF_DATA = (194, "Fake the Source of Data")
    PRINCIPAL_SPOOF = (195, "Principal Spoof")
    SESSION_CREDENTIAL_FALSIFICATION_THROUGH_FORGING = (
        196,
        "Session Credential Falsification through Forging",
    )
    EXPONENTIAL_DATA_EXPANSION = (197, "Exponential Data Expansion")
    XSS_TARGETING_ERROR_PAGES = (198, "XSS Targeting Error Pages")
    XSS_USING_ALTERNATE_SYNTAX = (199, "XSS Using Alternate Syntax")
    REMOVAL_OF_FILTERS_INPUT_FILTERS_OUTPUT_FILTERS_DATA_MASKING = (
        200,
        "Removal of filters: Input filters, output filters, data masking",
    )
    SERIALIZED_DATA_EXTERNAL_LINKING = (
        201,
        "Serialized Data External Linking",
    )
    CREATE_MALICIOUS_CLIENT = (202, "Create Malicious Client")
    MANIPULATE_REGISTRY_INFORMATION = (203, "Manipulate Registry Information")
    LIFTING_SENSITIVE_DATA_EMBEDDED_IN_CACHE = (
        204,
        "Lifting Sensitive Data Embedded in Cache",
    )
    SIGNING_MALICIOUS_CODE = (206, "Signing Malicious Code")
    REMOVING_IMPORTANT_CLIENT_FUNCTIONALITY = (
        207,
        "Removing Important Client Functionality",
    )
    REMOVINGSHORTCIRCUITING_PURSE_LOGIC_REMOVINGMUTATING_CASH_DECREMENTS = (
        208,
        "Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements",
    )
    XSS_USING_MIME_TYPE_MISMATCH = (209, "XSS Using MIME Type Mismatch")
    FUNCTIONALITY_MISUSE = (212, "Functionality Misuse")
    FUZZING_FOR_APPLICATION_MAPPING = (215, "Fuzzing for application mapping")
    COMMUNICATION_CHANNEL_MANIPULATION = (
        216,
        "Communication Channel Manipulation",
    )
    EXPLOITING_INCORRECTLY_CONFIGURED_SSLTLS = (
        217,
        "Exploiting Incorrectly Configured SSL/TLS",
    )
    SPOOFING_OF_UDDIEBXML_MESSAGES = (218, "Spoofing of UDDI/ebXML Messages")
    XML_ROUTING_DETOUR_ATTACKS = (219, "XML Routing Detour Attacks")
    CLIENTSERVER_PROTOCOL_MANIPULATION = (
        220,
        "Client-Server Protocol Manipulation",
    )
    DATA_SERIALIZATION_EXTERNAL_ENTITIES_BLOWUP = (
        221,
        "Data Serialization External Entities Blowup",
    )
    IFRAME_OVERLAY = (222, "iFrame Overlay")
    FINGERPRINTING = (224, "Fingerprinting")
    SESSION_CREDENTIAL_FALSIFICATION_THROUGH_MANIPULATION = (
        226,
        "Session Credential Falsification through Manipulation",
    )
    SUSTAINED_CLIENT_ENGAGEMENT = (227, "Sustained Client Engagement")
    DTD_INJECTION = (228, "DTD Injection")
    SERIALIZED_DATA_PARAMETER_BLOWUP = (
        229,
        "Serialized Data Parameter Blowup",
    )
    SERIALIZED_DATA_WITH_NESTED_PAYLOADS = (
        230,
        "Serialized Data with Nested Payloads",
    )
    OVERSIZED_SERIALIZED_DATA_PAYLOADS = (
        231,
        "Oversized Serialized Data Payloads",
    )
    PRIVILEGE_ESCALATION = (233, "Privilege Escalation")
    HIJACKING_A_PRIVILEGED_PROCESS = (234, "Hijacking a privileged process")
    ESCAPING_A_SANDBOX_BY_CALLING_CODE_IN_ANOTHER_LANGUAGE = (
        237,
        "Escaping a Sandbox by Calling Code in Another Language",
    )
    RESOURCE_INJECTION = (240, "Resource Injection")
    CODE_INJECTION = (242, "Code Injection")
    XSS_TARGETING_HTML_ATTRIBUTES = (243, "XSS Targeting HTML Attributes")
    XSS_TARGETING_URI_PLACEHOLDERS = (244, "XSS Targeting URI Placeholders")
    XSS_USING_DOUBLED_CHARACTERS = (245, "XSS Using Doubled Characters")
    XSS_USING_INVALID_CHARACTERS = (247, "XSS Using Invalid Characters")
    COMMAND_INJECTION = (248, "Command Injection")
    XML_INJECTION = (250, "XML Injection")
    LOCAL_CODE_INCLUSION = (251, "Local Code Inclusion")
    PHP_LOCAL_FILE_INCLUSION = (252, "PHP Local File Inclusion")
    REMOTE_CODE_INCLUSION = (253, "Remote Code Inclusion")
    SOAP_ARRAY_OVERFLOW = (256, "SOAP Array Overflow")
    FUZZING_FOR_GARNERING_OTHER_ADJACENT_USERSENSITIVE_DATA = (
        261,
        "Fuzzing for garnering other adjacent user/sensitive data",
    )
    FORCE_USE_OF_CORRUPTED_FILES = (263, "Force Use of Corrupted Files")
    LEVERAGE_ALTERNATE_ENCODING = (267, "Leverage Alternate Encoding")
    AUDIT_LOG_MANIPULATION = (268, "Audit Log Manipulation")
    MODIFICATION_OF_REGISTRY_RUN_KEYS = (
        270,
        "Modification of Registry Run Keys",
    )
    SCHEMA_POISONING = (271, "Schema Poisoning")
    PROTOCOL_MANIPULATION = (272, "Protocol Manipulation")
    HTTP_RESPONSE_SMUGGLING = (273, "HTTP Response Smuggling")
    HTTP_VERB_TAMPERING = (274, "HTTP Verb Tampering")
    DNS_REBINDING = (275, "DNS Rebinding")
    INTERCOMPONENT_PROTOCOL_MANIPULATION = (
        276,
        "Inter-component Protocol Manipulation",
    )
    DATA_INTERCHANGE_PROTOCOL_MANIPULATION = (
        277,
        "Data Interchange Protocol Manipulation",
    )
    WEB_SERVICES_PROTOCOL_MANIPULATION = (
        278,
        "Web Services Protocol Manipulation",
    )
    SOAP_MANIPULATION = (279, "SOAP Manipulation")
    ICMP_ECHO_REQUEST_PING = (285, "ICMP Echo Request Ping")
    TCP_SYN_SCAN = (287, "TCP SYN Scan")
    ENUMERATE_MAIL_EXCHANGE_MX_RECORDS = (
        290,
        "Enumerate Mail Exchange (MX) Records",
    )
    DNS_ZONE_TRANSFERS = (291, "DNS Zone Transfers")
    HOST_DISCOVERY = (292, "Host Discovery")
    TRACEROUTE_ROUTE_ENUMERATION = (293, "Traceroute Route Enumeration")
    ICMP_ADDRESS_MASK_REQUEST = (294, "ICMP Address Mask Request")
    TIMESTAMP_REQUEST = (295, "Timestamp Request")
    ICMP_INFORMATION_REQUEST = (296, "ICMP Information Request")
    TCP_ACK_PING = (297, "TCP ACK Ping")
    UDP_PING = (298, "UDP Ping")
    TCP_SYN_PING = (299, "TCP SYN Ping")
    PORT_SCANNING = (300, "Port Scanning")
    TCP_CONNECT_SCAN = (301, "TCP Connect Scan")
    TCP_FIN_SCAN = (302, "TCP FIN Scan")
    TCP_XMAS_SCAN = (303, "TCP Xmas Scan")
    TCP_NULL_SCAN = (304, "TCP Null Scan")
    TCP_ACK_SCAN = (305, "TCP ACK Scan")
    TCP_WINDOW_SCAN = (306, "TCP Window Scan")
    TCP_RPC_SCAN = (307, "TCP RPC Scan")
    UDP_SCAN = (308, "UDP Scan")
    NETWORK_TOPOLOGY_MAPPING = (309, "Network Topology Mapping")
    SCANNING_FOR_VULNERABLE_SOFTWARE = (
        310,
        "Scanning for Vulnerable Software",
    )
    ACTIVE_OS_FINGERPRINTING = (312, "Active OS Fingerprinting")
    PASSIVE_OS_FINGERPRINTING = (313, "Passive OS Fingerprinting")
    IP_ID_SEQUENCING_PROBE = (317, "IP ID Sequencing Probe")
    IP_ID_ECHOED_BYTEORDER_PROBE = (318, "IP 'ID' Echoed Byte-Order Probe")
    IP_DF_DONT_FRAGMENT_BIT_ECHOING_PROBE = (
        319,
        "IP (DF) 'Don't Fragment Bit' Echoing Probe",
    )
    TCP_TIMESTAMP_PROBE = (320, "TCP Timestamp Probe")
    TCP_SEQUENCE_NUMBER_PROBE = (321, "TCP Sequence Number Probe")
    TCP_ISN_GREATEST_COMMON_DIVISOR_PROBE = (
        322,
        "TCP (ISN) Greatest Common Divisor Probe",
    )
    TCP_ISN_COUNTER_RATE_PROBE = (323, "TCP (ISN) Counter Rate Probe")
    TCP_ISN_SEQUENCE_PREDICTABILITY_PROBE = (
        324,
        "TCP (ISN) Sequence Predictability Probe",
    )
    TCP_CONGESTION_CONTROL_FLAG_ECN_PROBE = (
        325,
        "TCP Congestion Control Flag (ECN) Probe",
    )
    TCP_INITIAL_WINDOW_SIZE_PROBE = (326, "TCP Initial Window Size Probe")
    TCP_OPTIONS_PROBE = (327, "TCP Options Probe")
    TCP_RST_FLAG_CHECKSUM_PROBE = (328, "TCP 'RST' Flag Checksum Probe")
    ICMP_ERROR_MESSAGE_QUOTING_PROBE = (
        329,
        "ICMP Error Message Quoting Probe",
    )
    ICMP_ERROR_MESSAGE_ECHOING_INTEGRITY_PROBE = (
        330,
        "ICMP Error Message Echoing Integrity Probe",
    )
    ICMP_IP_TOTAL_LENGTH_FIELD_PROBE = (
        331,
        "ICMP IP Total Length Field Probe",
    )
    ICMP_IP_ID_FIELD_ERROR_MESSAGE_PROBE = (
        332,
        "ICMP IP 'ID' Field Error Message Probe",
    )
    HARVESTING_INFORMATION_VIA_API_EVENT_MONITORING = (
        383,
        "Harvesting Information via API Event Monitoring",
    )
    APPLICATION_API_MESSAGE_MANIPULATION_VIA_MANINTHEMIDDLE = (
        384,
        "Application API Message Manipulation via Man-in-the-Middle",
    )
    TRANSACTION_OR_EVENT_TAMPERING_VIA_APPLICATION_API_MANIPULATION = (
        385,
        "Transaction or Event Tampering via Application API Manipulation",
    )
    APPLICATION_API_NAVIGATION_REMAPPING = (
        386,
        "Application API Navigation Remapping",
    )
    NAVIGATION_REMAPPING_TO_PROPAGATE_MALICIOUS_CONTENT = (
        387,
        "Navigation Remapping To Propagate Malicious Content",
    )
    APPLICATION_API_BUTTON_HIJACKING = (
        388,
        "Application API Button Hijacking",
    )
    CONTENT_SPOOFING_VIA_APPLICATION_API_MANIPULATION = (
        389,
        "Content Spoofing Via Application API Manipulation",
    )
    BYPASSING_PHYSICAL_SECURITY = (390, "Bypassing Physical Security")
    BYPASSING_PHYSICAL_LOCKS = (391, "Bypassing Physical Locks")
    LOCK_BUMPING = (392, "Lock Bumping")
    LOCK_PICKING = (393, "Lock Picking")
    USING_A_SNAP_GUN_LOCK_TO_FORCE_A_LOCK = (
        394,
        "Using a Snap Gun Lock to Force a Lock",
    )
    BYPASSING_ELECTRONIC_LOCKS_AND_ACCESS_CONTROLS = (
        395,
        "Bypassing Electronic Locks and Access Controls",
    )
    CLONING_MAGNETIC_STRIP_CARDS = (397, "Cloning Magnetic Strip Cards")
    MAGNETIC_STRIP_CARD_BRUTE_FORCE_ATTACKS = (
        398,
        "Magnetic Strip Card Brute Force Attacks",
    )
    CLONING_RFID_CARDS_OR_CHIPS = (399, "Cloning RFID Cards or Chips")
    RFID_CHIP_DEACTIVATION_OR_DESTRUCTION = (
        400,
        "RFID Chip Deactivation or Destruction",
    )
    PHYSICALLY_HACKING_HARDWARE = (401, "Physically Hacking Hardware")
    BYPASSING_ATA_PASSWORD_SECURITY = (402, "Bypassing ATA Password Security")
    DUMPSTER_DIVING = (406, "Dumpster Diving")
    PRETEXTING = (407, "Pretexting")
    INFORMATION_ELICITATION = (410, "Information Elicitation")
    PRETEXTING_VIA_CUSTOMER_SERVICE = (412, "Pretexting via Customer Service")
    PRETEXTING_VIA_TECH_SUPPORT = (413, "Pretexting via Tech Support")
    PRETEXTING_VIA_DELIVERY_PERSON = (414, "Pretexting via Delivery Person")
    PRETEXTING_VIA_PHONE = (415, "Pretexting via Phone")
    MANIPULATE_HUMAN_BEHAVIOR = (416, "Manipulate Human Behavior")
    INFLUENCE_PERCEPTION = (417, "Influence Perception")
    INFLUENCE_PERCEPTION_OF_RECIPROCATION = (
        418,
        "Influence Perception of Reciprocation",
    )
    INFLUENCE_PERCEPTION_OF_SCARCITY = (
        420,
        "Influence Perception of Scarcity",
    )
    INFLUENCE_PERCEPTION_OF_AUTHORITY = (
        421,
        "Influence Perception of Authority",
    )
    INFLUENCE_PERCEPTION_OF_COMMITMENT_AND_CONSISTENCY = (
        422,
        "Influence Perception of Commitment and Consistency",
    )
    INFLUENCE_PERCEPTION_OF_LIKING = (423, "Influence Perception of Liking")
    INFLUENCE_PERCEPTION_OF_CONSENSUS_OR_SOCIAL_PROOF = (
        424,
        "Influence Perception of Consensus or Social Proof",
    )
    TARGET_INFLUENCE_VIA_FRAMING = (425, "Target Influence via Framing")
    INFLUENCE_VIA_INCENTIVES = (426, "Influence via Incentives")
    INFLUENCE_VIA_PSYCHOLOGICAL_PRINCIPLES = (
        427,
        "Influence via Psychological Principles",
    )
    INFLUENCE_VIA_MODES_OF_THINKING = (428, "Influence via Modes of Thinking")
    TARGET_INFLUENCE_VIA_EYE_CUES = (429, "Target Influence via Eye Cues")
    TARGET_INFLUENCE_VIA_THE_HUMAN_BUFFER_OVERFLOW = (
        433,
        "Target Influence via The Human Buffer Overflow",
    )
    TARGET_INFLUENCE_VIA_INTERVIEW_AND_INTERROGATION = (
        434,
        "Target Influence via Interview and Interrogation",
    )
    TARGET_INFLUENCE_VIA_INSTANT_RAPPORT = (
        435,
        "Target Influence via Instant Rapport",
    )
    MODIFICATION_DURING_MANUFACTURE = (438, "Modification During Manufacture")
    MANIPULATION_DURING_DISTRIBUTION = (
        439,
        "Manipulation During Distribution",
    )
    HARDWARE_INTEGRITY_ATTACK = (440, "Hardware Integrity Attack")
    MALICIOUS_LOGIC_INSERTION = (441, "Malicious Logic Insertion")
    INFECTED_SOFTWARE = (442, "Infected Software")
    MALICIOUS_LOGIC_INSERTED_INTO_PRODUCT_BY_AUTHORIZED_DEVELOPER = (
        443,
        "Malicious Logic Inserted Into Product by Authorized Developer",
    )
    DEVELOPMENT_ALTERATION = (444, "Development Alteration")
    MALICIOUS_LOGIC_INSERTION_INTO_PRODUCT_SOFTWARE_VIA_CONFIGURATION_MANAGEMENT_MANIPULATION = (
        445,
        "Malicious Logic Insertion into Product Software via Configuration Management Manipulation",
    )
    MALICIOUS_LOGIC_INSERTION_INTO_PRODUCT_VIA_INCLUSION_OF_THIRDPARTY_COMPONENT = (
        446,
        "Malicious Logic Insertion into Product via Inclusion of Third-Party Component",
    )
    DESIGN_ALTERATION = (447, "Design Alteration")
    EMBED_VIRUS_INTO_DLL = (448, "Embed Virus into DLL")
    INFECTED_HARDWARE = (452, "Infected Hardware")
    INFECTED_MEMORY = (456, "Infected Memory")
    USB_MEMORY_ATTACKS = (457, "USB Memory Attacks")
    FLASH_MEMORY_ATTACKS = (458, "Flash Memory Attacks")
    CREATING_A_ROGUE_CERTIFICATION_AUTHORITY_CERTIFICATE = (
        459,
        "Creating a Rogue Certification Authority Certificate",
    )
    HTTP_PARAMETER_POLLUTION_HPP = (460, "HTTP Parameter Pollution (HPP)")
    WEB_SERVICES_API_SIGNATURE_FORGERY_LEVERAGING_HASH_FUNCTION_EXTENSION_WEAKNESS = (
        461,
        "Web Services API Signature Forgery Leveraging Hash Function Extension Weakness",
    )
    CROSSDOMAIN_SEARCH_TIMING = (462, "Cross-Domain Search Timing")
    PADDING_ORACLE_CRYPTO_ATTACK = (463, "Padding Oracle Crypto Attack")
    EVERCOOKIE = (464, "Evercookie")
    TRANSPARENT_PROXY_ABUSE = (465, "Transparent Proxy Abuse")
    LEVERAGING_ACTIVE_ADVERSARY_IN_THE_MIDDLE_ATTACKS_TO_BYPASS_SAME_ORIGIN_POLICY = (
        466,
        "Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy",
    )
    CROSS_SITE_IDENTIFICATION = (467, "Cross Site Identification")
    GENERIC_CROSSBROWSER_CROSSDOMAIN_THEFT = (
        468,
        "Generic Cross-Browser Cross-Domain Theft",
    )
    HTTP_DOS = (469, "HTTP DoS")
    EXPANDING_CONTROL_OVER_THE_OPERATING_SYSTEM_FROM_THE_DATABASE = (
        470,
        "Expanding Control over the Operating System from the Database",
    )
    SEARCH_ORDER_HIJACKING = (471, "Search Order Hijacking")
    BROWSER_FINGERPRINTING = (472, "Browser Fingerprinting")
    SIGNATURE_SPOOF = (473, "Signature Spoof")
    SIGNATURE_SPOOFING_BY_KEY_THEFT = (474, "Signature Spoofing by Key Theft")
    SIGNATURE_SPOOFING_BY_IMPROPER_VALIDATION = (
        475,
        "Signature Spoofing by Improper Validation",
    )
    SIGNATURE_SPOOFING_BY_MISREPRESENTATION = (
        476,
        "Signature Spoofing by Misrepresentation",
    )
    SIGNATURE_SPOOFING_BY_MIXING_SIGNED_AND_UNSIGNED_CONTENT = (
        477,
        "Signature Spoofing by Mixing Signed and Unsigned Content",
    )
    MODIFICATION_OF_WINDOWS_SERVICE_CONFIGURATION = (
        478,
        "Modification of Windows Service Configuration",
    )
    MALICIOUS_ROOT_CERTIFICATE = (479, "Malicious Root Certificate")
    ESCAPING_VIRTUALIZATION = (480, "Escaping Virtualization")
    CONTRADICTORY_DESTINATIONS_IN_TRAFFIC_ROUTING_SCHEMES = (
        481,
        "Contradictory Destinations in Traffic Routing Schemes",
    )
    TCP_FLOOD = (482, "TCP Flood")
    SIGNATURE_SPOOFING_BY_KEY_RECREATION = (
        485,
        "Signature Spoofing by Key Recreation",
    )
    UDP_FLOOD = (486, "UDP Flood")
    ICMP_FLOOD = (487, "ICMP Flood")
    HTTP_FLOOD = (488, "HTTP Flood")
    SSL_FLOOD = (489, "SSL Flood")
    AMPLIFICATION = (490, "Amplification")
    QUADRATIC_DATA_EXPANSION = (491, "Quadratic Data Expansion")
    REGULAR_EXPRESSION_EXPONENTIAL_BLOWUP = (
        492,
        "Regular Expression Exponential Blowup",
    )
    SOAP_ARRAY_BLOWUP = (493, "SOAP Array Blowup")
    TCP_FRAGMENTATION = (494, "TCP Fragmentation")
    UDP_FRAGMENTATION = (495, "UDP Fragmentation")
    ICMP_FRAGMENTATION = (496, "ICMP Fragmentation")
    FILE_DISCOVERY = (497, "File Discovery")
    PROBE_IOS_SCREENSHOTS = (498, "Probe iOS Screenshots")
    ANDROID_INTENT_INTERCEPT = (499, "Android Intent Intercept")
    WEBVIEW_INJECTION = (500, "WebView Injection")
    ANDROID_ACTIVITY_HIJACK = (501, "Android Activity Hijack")
    INTENT_SPOOF = (502, "Intent Spoof")
    WEBVIEW_EXPOSURE = (503, "WebView Exposure")
    TASK_IMPERSONATION = (504, "Task Impersonation")
    SCHEME_SQUATTING = (505, "Scheme Squatting")
    TAPJACKING = (506, "Tapjacking")
    PHYSICAL_THEFT = (507, "Physical Theft")
    SHOULDER_SURFING = (508, "Shoulder Surfing")
    KERBEROASTING = (509, "Kerberoasting")
    SAAS_USER_REQUEST_FORGERY = (510, "SaaS User Request Forgery")
    INFILTRATION_OF_SOFTWARE_DEVELOPMENT_ENVIRONMENT = (
        511,
        "Infiltration of Software Development Environment",
    )
    HARDWARE_COMPONENT_SUBSTITUTION_DURING_BASELINING = (
        516,
        "Hardware Component Substitution During Baselining",
    )
    DOCUMENTATION_ALTERATION_TO_CIRCUMVENT_DIALDOWN = (
        517,
        "Documentation Alteration to Circumvent Dial-down",
    )
    DOCUMENTATION_ALTERATION_TO_PRODUCE_UNDERPERFORMING_SYSTEMS = (
        518,
        "Documentation Alteration to Produce Under-performing Systems",
    )
    DOCUMENTATION_ALTERATION_TO_CAUSE_ERRORS_IN_SYSTEM_DESIGN = (
        519,
        "Documentation Alteration to Cause Errors in System Design",
    )
    COUNTERFEIT_HARDWARE_COMPONENT_INSERTED_DURING_PRODUCT_ASSEMBLY = (
        520,
        "Counterfeit Hardware Component Inserted During Product Assembly",
    )
    HARDWARE_DESIGN_SPECIFICATIONS_ARE_ALTERED = (
        521,
        "Hardware Design Specifications Are Altered",
    )
    MALICIOUS_HARDWARE_COMPONENT_REPLACEMENT = (
        522,
        "Malicious Hardware Component Replacement",
    )
    MALICIOUS_SOFTWARE_IMPLANTED = (523, "Malicious Software Implanted")
    ROGUE_INTEGRATION_PROCEDURES = (524, "Rogue Integration Procedures")
    XML_FLOOD = (528, "XML Flood")
    MALWAREDIRECTED_INTERNAL_RECONNAISSANCE = (
        529,
        "Malware-Directed Internal Reconnaissance",
    )
    PROVIDE_COUNTERFEIT_COMPONENT = (530, "Provide Counterfeit Component")
    HARDWARE_COMPONENT_SUBSTITUTION = (531, "Hardware Component Substitution")
    ALTERED_INSTALLED_BIOS = (532, "Altered Installed BIOS")
    MALICIOUS_MANUAL_SOFTWARE_UPDATE = (
        533,
        "Malicious Manual Software Update",
    )
    MALICIOUS_HARDWARE_UPDATE = (534, "Malicious Hardware Update")
    MALICIOUS_GRAY_MARKET_HARDWARE = (535, "Malicious Gray Market Hardware")
    DATA_INJECTED_DURING_CONFIGURATION = (
        536,
        "Data Injected During Configuration",
    )
    INFILTRATION_OF_HARDWARE_DEVELOPMENT_ENVIRONMENT = (
        537,
        "Infiltration of Hardware Development Environment",
    )
    OPENSOURCE_LIBRARY_MANIPULATION = (538, "Open-Source Library Manipulation")
    ASIC_WITH_MALICIOUS_FUNCTIONALITY = (
        539,
        "ASIC With Malicious Functionality",
    )
    OVERREAD_BUFFERS = (540, "Overread Buffers")
    APPLICATION_FINGERPRINTING = (541, "Application Fingerprinting")
    TARGETED_MALWARE = (542, "Targeted Malware")
    COUNTERFEIT_WEBSITES = (543, "Counterfeit Websites")
    COUNTERFEIT_ORGANIZATIONS = (544, "Counterfeit Organizations")
    PULL_DATA_FROM_SYSTEM_RESOURCES = (545, "Pull Data from System Resources")
    INCOMPLETE_DATA_DELETION_IN_A_MULTITENANT_ENVIRONMENT = (
        546,
        "Incomplete Data Deletion in a Multi-Tenant Environment",
    )
    PHYSICAL_DESTRUCTION_OF_DEVICE_OR_COMPONENT = (
        547,
        "Physical Destruction of Device or Component",
    )
    CONTAMINATE_RESOURCE = (548, "Contaminate Resource")
    LOCAL_EXECUTION_OF_CODE = (549, "Local Execution of Code")
    INSTALL_NEW_SERVICE = (550, "Install New Service")
    MODIFY_EXISTING_SERVICE = (551, "Modify Existing Service")
    INSTALL_ROOTKIT_ = (552, "Install Rootkit ")
    FUNCTIONALITY_BYPASS = (554, "Functionality Bypass")
    REMOTE_SERVICES_WITH_STOLEN_CREDENTIALS = (
        555,
        "Remote Services with Stolen Credentials",
    )
    REPLACE_FILE_EXTENSION_HANDLERS = (556, "Replace File Extension Handlers")
    REPLACE_TRUSTED_EXECUTABLE = (558, "Replace Trusted Executable")
    ORBITAL_JAMMING = (559, "Orbital Jamming")
    USE_OF_KNOWN_DOMAIN_CREDENTIALS = (560, "Use of Known Domain Credentials")
    WINDOWS_ADMIN_SHARES_WITH_STOLEN_CREDENTIALS = (
        561,
        "Windows Admin Shares with Stolen Credentials",
    )
    MODIFY_SHARED_FILE = (562, "Modify Shared File")
    ADD_MALICIOUS_FILE_TO_SHARED_WEBROOT = (
        563,
        "Add Malicious File to Shared Webroot",
    )
    RUN_SOFTWARE_AT_LOGON = (564, "Run Software at Logon")
    PASSWORD_SPRAYING = (565, "Password Spraying")
    CAPTURE_CREDENTIALS_VIA_KEYLOGGER = (
        568,
        "Capture Credentials via Keylogger",
    )
    COLLECT_DATA_AS_PROVIDED_BY_USERS = (
        569,
        "Collect Data as Provided by Users",
    )
    BLOCK_LOGGING_TO_CENTRAL_REPOSITORY = (
        571,
        "Block Logging to Central Repository",
    )
    ARTIFICIALLY_INFLATE_FILE_SIZES = (572, "Artificially Inflate File Sizes")
    PROCESS_FOOTPRINTING = (573, "Process Footprinting")
    SERVICES_FOOTPRINTING = (574, "Services Footprinting")
    ACCOUNT_FOOTPRINTING = (575, "Account Footprinting")
    GROUP_PERMISSION_FOOTPRINTING = (576, "Group Permission Footprinting")
    OWNER_FOOTPRINTING = (577, "Owner Footprinting")
    DISABLE_SECURITY_SOFTWARE = (578, "Disable Security Software")
    REPLACE_WINLOGON_HELPER_DLL = (579, "Replace Winlogon Helper DLL")
    SYSTEM_FOOTPRINTING = (580, "System Footprinting")
    SECURITY_SOFTWARE_FOOTPRINTING = (581, "Security Software Footprinting")
    ROUTE_DISABLING = (582, "Route Disabling")
    DISABLING_NETWORK_HARDWARE = (583, "Disabling Network Hardware")
    BGP_ROUTE_DISABLING = (584, "BGP Route Disabling")
    DNS_DOMAIN_SEIZURE = (585, "DNS Domain Seizure")
    OBJECT_INJECTION = (586, "Object Injection")
    CROSS_FRAME_SCRIPTING_XFS = (587, "Cross Frame Scripting (XFS)")
    DOMBASED_XSS = (588, "DOM-Based XSS")
    DNS_BLOCKING = (589, "DNS Blocking")
    IP_ADDRESS_BLOCKING = (590, "IP Address Blocking")
    REFLECTED_XSS = (591, "Reflected XSS")
    STORED_XSS = (592, "Stored XSS")
    SESSION_HIJACKING = (593, "Session Hijacking")
    TRAFFIC_INJECTION = (594, "Traffic Injection")
    CONNECTION_RESET = (595, "Connection Reset")
    TCP_RST_INJECTION = (596, "TCP RST Injection")
    ABSOLUTE_PATH_TRAVERSAL = (597, "Absolute Path Traversal")
    DNS_SPOOFING = (598, "DNS Spoofing")
    TERRESTRIAL_JAMMING = (599, "Terrestrial Jamming")
    CREDENTIAL_STUFFING = (600, "Credential Stuffing")
    JAMMING = (601, "Jamming")
    BLOCKAGE = (603, "Blockage")
    WIFI_JAMMING = (604, "Wi-Fi Jamming")
    CELLULAR_JAMMING = (605, "Cellular Jamming")
    WEAKENING_OF_CELLULAR_ENCRYPTION = (
        606,
        "Weakening of Cellular Encryption",
    )
    OBSTRUCTION = (607, "Obstruction")
    CRYPTANALYSIS_OF_CELLULAR_ENCRYPTION = (
        608,
        "Cryptanalysis of Cellular Encryption",
    )
    CELLULAR_TRAFFIC_INTERCEPT = (609, "Cellular Traffic Intercept")
    CELLULAR_DATA_INJECTION = (610, "Cellular Data Injection")
    BITSQUATTING = (611, "BitSquatting")
    WIFI_MAC_ADDRESS_TRACKING = (612, "WiFi MAC Address Tracking")
    WIFI_SSID_TRACKING = (613, "WiFi SSID Tracking")
    ROOTING_SIM_CARDS = (614, "Rooting SIM Cards")
    EVIL_TWIN_WIFI_ATTACK = (615, "Evil Twin Wi-Fi Attack")
    ESTABLISH_ROGUE_LOCATION = (616, "Establish Rogue Location")
    CELLULAR_ROGUE_BASE_STATION = (617, "Cellular Rogue Base Station")
    CELLULAR_BROADCAST_MESSAGE_REQUEST = (
        618,
        "Cellular Broadcast Message Request",
    )
    SIGNAL_STRENGTH_TRACKING = (619, "Signal Strength Tracking")
    DROP_ENCRYPTION_LEVEL = (620, "Drop Encryption Level")
    ANALYSIS_OF_PACKET_TIMING_AND_SIZES = (
        621,
        "Analysis of Packet Timing and Sizes",
    )
    ELECTROMAGNETIC_SIDECHANNEL_ATTACK = (
        622,
        "Electromagnetic Side-Channel Attack",
    )
    COMPROMISING_EMANATIONS_ATTACK = (623, "Compromising Emanations Attack")
    HARDWARE_FAULT_INJECTION = (624, "Hardware Fault Injection")
    MOBILE_DEVICE_FAULT_INJECTION = (625, "Mobile Device Fault Injection")
    SMUDGE_ATTACK = (626, "Smudge Attack")
    COUNTERFEIT_GPS_SIGNALS = (627, "Counterfeit GPS Signals")
    CARRYOFF_GPS_ATTACK = (628, "Carry-Off GPS Attack")
    TYPOSQUATTING = (630, "TypoSquatting")
    SOUNDSQUATTING = (631, "SoundSquatting")
    HOMOGRAPH_ATTACK_VIA_HOMOGLYPHS = (632, "Homograph Attack via Homoglyphs")
    TOKEN_IMPERSONATION = (633, "Token Impersonation")
    PROBE_AUDIO_AND_VIDEO_PERIPHERALS = (
        634,
        "Probe Audio and Video Peripherals",
    )
    ALTERNATIVE_EXECUTION_DUE_TO_DECEPTIVE_FILENAMES = (
        635,
        "Alternative Execution Due to Deceptive Filenames",
    )
    HIDING_MALICIOUS_DATA_OR_CODE_WITHIN_FILES = (
        636,
        "Hiding Malicious Data or Code within Files",
    )
    COLLECT_DATA_FROM_CLIPBOARD = (637, "Collect Data from Clipboard")
    ALTERED_COMPONENT_FIRMWARE = (638, "Altered Component Firmware")
    PROBE_SYSTEM_FILES = (639, "Probe System Files")
    INCLUSION_OF_CODE_IN_EXISTING_PROCESS = (
        640,
        "Inclusion of Code in Existing Process",
    )
    DLL_SIDELOADING = (641, "DLL Side-Loading")
    REPLACE_BINARIES = (642, "Replace Binaries")
    IDENTIFY_SHARED_FILESDIRECTORIES_ON_SYSTEM = (
        643,
        "Identify Shared Files/Directories on System",
    )
    USE_OF_CAPTURED_HASHES_PASS_THE_HASH = (
        644,
        "Use of Captured Hashes (Pass The Hash)",
    )
    USE_OF_CAPTURED_TICKETS_PASS_THE_TICKET = (
        645,
        "Use of Captured Tickets (Pass The Ticket)",
    )
    PERIPHERAL_FOOTPRINTING = (646, "Peripheral Footprinting")
    COLLECT_DATA_FROM_REGISTRIES = (647, "Collect Data from Registries")
    COLLECT_DATA_FROM_SCREEN_CAPTURE = (
        648,
        "Collect Data from Screen Capture",
    )
    ADDING_A_SPACE_TO_A_FILE_EXTENSION = (
        649,
        "Adding a Space to a File Extension",
    )
    UPLOAD_A_WEB_SHELL_TO_A_WEB_SERVER = (
        650,
        "Upload a Web Shell to a Web Server",
    )
    EAVESDROPPING = (651, "Eavesdropping")
    USE_OF_KNOWN_KERBEROS_CREDENTIALS = (
        652,
        "Use of Known Kerberos Credentials",
    )
    USE_OF_KNOWN_OPERATING_SYSTEM_CREDENTIALS = (
        653,
        "Use of Known Operating System Credentials",
    )
    CREDENTIAL_PROMPT_IMPERSONATION = (654, "Credential Prompt Impersonation")
    AVOID_SECURITY_TOOL_IDENTIFICATION_BY_ADDING_DATA = (
        655,
        "Avoid Security Tool Identification by Adding Data",
    )
    VOICE_PHISHING = (656, "Voice Phishing")
    MALICIOUS_AUTOMATED_SOFTWARE_UPDATE_VIA_SPOOFING = (
        657,
        "Malicious Automated Software Update via Spoofing",
    )
    ROOTJAILBREAK_DETECTION_EVASION_VIA_HOOKING = (
        660,
        "Root/Jailbreak Detection Evasion via Hooking",
    )
    ROOTJAILBREAK_DETECTION_EVASION_VIA_DEBUGGING = (
        661,
        "Root/Jailbreak Detection Evasion via Debugging",
    )
    ADVERSARY_IN_THE_BROWSER_AITB = (662, "Adversary in the Browser (AiTB)")
    EXPLOITATION_OF_TRANSIENT_INSTRUCTION_EXECUTION = (
        663,
        "Exploitation of Transient Instruction Execution",
    )
    SERVER_SIDE_REQUEST_FORGERY = (664, "Server Side Request Forgery")
    EXPLOITATION_OF_THUNDERBOLT_PROTECTION_FLAWS = (
        665,
        "Exploitation of Thunderbolt Protection Flaws",
    )
    BLUESMACKING = (666, "BlueSmacking")
    BLUETOOTH_IMPERSONATION_ATTACKS_BIAS = (
        667,
        "Bluetooth Impersonation AttackS (BIAS)",
    )
    KEY_NEGOTIATION_OF_BLUETOOTH_ATTACK_KNOB = (
        668,
        "Key Negotiation of Bluetooth Attack (KNOB)",
    )
    ALTERATION_OF_A_SOFTWARE_UPDATE = (669, "Alteration of a Software Update")
    SOFTWARE_DEVELOPMENT_TOOLS_MALICIOUSLY_ALTERED = (
        670,
        "Software Development Tools Maliciously Altered",
    )
    REQUIREMENTS_FOR_ASIC_FUNCTIONALITY_MALICIOUSLY_ALTERED = (
        671,
        "Requirements for ASIC Functionality Maliciously Altered",
    )
    MALICIOUS_CODE_IMPLANTED_DURING_CHIP_PROGRAMMING = (
        672,
        "Malicious Code Implanted During Chip Programming",
    )
    DEVELOPER_SIGNING_MALICIOUSLY_ALTERED_SOFTWARE = (
        673,
        "Developer Signing Maliciously Altered Software",
    )
    DESIGN_FOR_FPGA_MALICIOUSLY_ALTERED = (
        674,
        "Design for FPGA Maliciously Altered",
    )
    RETRIEVE_DATA_FROM_DECOMMISSIONED_DEVICES = (
        675,
        "Retrieve Data from Decommissioned Devices",
    )
    NOSQL_INJECTION = (676, "NoSQL Injection")
    SERVER_MOTHERBOARD_COMPROMISE = (677, "Server Motherboard Compromise")
    SYSTEM_BUILD_DATA_MALICIOUSLY_ALTERED = (
        678,
        "System Build Data Maliciously Altered",
    )
    EXPLOITATION_OF_IMPROPERLY_CONFIGURED_OR_IMPLEMENTED_MEMORY_PROTECTIONS = (
        679,
        "Exploitation of Improperly Configured or Implemented Memory Protections",
    )
    EXPLOITATION_OF_IMPROPERLY_CONTROLLED_REGISTERS = (
        680,
        "Exploitation of Improperly Controlled Registers",
    )
    EXPLOITATION_OF_IMPROPERLY_CONTROLLED_HARDWARE_SECURITY_IDENTIFIERS = (
        681,
        "Exploitation of Improperly Controlled Hardware Security Identifiers",
    )
    EXPLOITATION_OF_FIRMWARE_OR_ROM_CODE_WITH_UNPATCHABLE_VULNERABILITIES = (
        682,
        "Exploitation of Firmware or ROM Code with Unpatchable Vulnerabilities",
    )
    METADATA_SPOOFING = (690, "Metadata Spoofing")
    SPOOF_OPENSOURCE_SOFTWARE_METADATA = (
        691,
        "Spoof Open-Source Software Metadata",
    )
    SPOOF_VERSION_CONTROL_SYSTEM_COMMIT_METADATA = (
        692,
        "Spoof Version Control System Commit Metadata",
    )
    STARJACKING = (693, "StarJacking")
    SYSTEM_LOCATION_DISCOVERY = (694, "System Location Discovery")
    REPO_JACKING = (695, "Repo Jacking")
    LOAD_VALUE_INJECTION = (696, "Load Value Injection")
    DHCP_SPOOFING = (697, "DHCP Spoofing")
    INSTALL_MALICIOUS_EXTENSION = (698, "Install Malicious Extension")
    EAVESDROPPING_ON_A_MONITOR = (699, "Eavesdropping on a Monitor")
    NETWORK_BOUNDARY_BRIDGING = (700, "Network Boundary Bridging")
    BROWSER_IN_THE_MIDDLE_BITM = (701, "Browser in the Middle (BiTM)")
    EXPLOITING_INCORRECT_CHAINING_OR_GRANULARITY_OF_HARDWARE_DEBUG_COMPONENTS = (
        702,
        "Exploiting Incorrect Chaining or Granularity of Hardware Debug Components",
    )

    def __new__(cls, id, name):
        obj = object.__new__(cls)
        obj._value_ = id
        obj.name_ = name
        return obj

    @property
    def name(self):
        return self.name_

    @classmethod
    def from_name(cls, name):
        if not hasattr(cls, f"_{cls.__name__}__name_to_key"):
            cls.__name_to_key = {v.name: v for v in cls}
        key = cls.__name_to_key.get(name)
        if key is None:
            raise ValueError(f"No external-reference CAPEC found for {name}.")
        return key

    @classmethod
    def from_id(cls, id):
        if not hasattr(cls, f"_{cls.__name__}__id_to_key"):
            cls.__id_to_key = {v.value: v for v in cls}
        key = cls.__id_to_key.get(int(id))
        if key is None:
            raise ValueError(f"No external-reference CAPEC found for {id}.")
        return key
