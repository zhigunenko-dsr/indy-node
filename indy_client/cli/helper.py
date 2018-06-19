from indy_client.cli.constants import \
    CLIENT_GRAMS_CLIENT_WITH_DID_FORMATTED_REG_EX, \
    CLIENT_GRAMS_CLIENT_ADD_FORMATTED_REG_EX, SEND_NYM_FORMATTED_REG_EX, \
    GET_NYM_FORMATTED_REG_EX, \
    GET_ATTR_FORMATTED_REG_EX, GET_SCHEMA_FORMATTED_REG_EX, \
    GET_CLAIM_DEF_FORMATTED_REG_EX, \
    ADD_ATTRIB_FORMATTED_REG_EX, SEND_SCHEMA_FORMATTED_REG_EX, \
    ADD_GENESIS_FORMATTED_REG_EX, \
    INIT_ATTR_REPO_FORMATTED_REG_EX, ADD_ATTRS_FORMATTED_REG_EX, \
    ADD_ATTRS_PROVER_FORMATTED_REG_EX, CONNECT_FORMATTED_REG_EX, \
    SHOW_FILE_FORMATTED_REG_EX, LOAD_FILE_FORMATTED_REG_EX, \
    SHOW_LINK_FORMATTED_REG_EX, SYNC_LINK_FORMATTED_REG_EX, \
    ACCEPT_LINK_FORMATTED_REG_EX, SHOW_CLAIM_FORMATTED_REG_EX, \
    LIST_CLAIMS_FORMATTED_REG_EX, REQUEST_CLAIM_FORMATTED_REG_EX, \
    SET_ATTRIBUTE_FORMATTED_REG_EX, SHOW_PROOF_REQ_FORMATTED_REG_EX, \
    SEND_CLAIM_DEF_FORMATTED_REG_EX, SEND_PROOF_FORMATTED_REG_EX, \
    PING_TARGET_FORMATTED_REG_EX, SEND_NODE_FORMATTED_REG_EX, \
    SEND_POOL_UPG_FORMATTED_REG_EX, DISCONNECT_FORMATTED_REG_EX, \
    NEW_ID_FORMATTED_REG_EX, SEND_PROOF_REQ_FORMATTED_REG_EX, \
    REQ_AVAIL_CLAIMS_FORMATTED_REG_EX, LIST_LINKS_FORMATTED_REG_EX, SEND_POOL_CONFIG_FORMATTED_REG_EX, \
    CHANGE_CURRENT_KEY_FORMATTED_REG_EX
# SHOW_CLAIM_REQ_FORMATTED_REG_EX


def getNewClientGrams():
    # TODO: Why do we have to manually pipe each regex except the last
    # one? Fix this
    return [
        ADD_GENESIS_FORMATTED_REG_EX,
        # Regex for `new client steward with DID <nym>`
        CLIENT_GRAMS_CLIENT_WITH_DID_FORMATTED_REG_EX,
        # Regex for `client steward add TRUST ANCHOR bob` or `client steward
        # add user bob`
        CLIENT_GRAMS_CLIENT_ADD_FORMATTED_REG_EX,
        SEND_NYM_FORMATTED_REG_EX,
        GET_NYM_FORMATTED_REG_EX,
        ADD_ATTRIB_FORMATTED_REG_EX,
        GET_ATTR_FORMATTED_REG_EX,
        SEND_SCHEMA_FORMATTED_REG_EX,
        GET_SCHEMA_FORMATTED_REG_EX,
        SEND_CLAIM_DEF_FORMATTED_REG_EX,
        GET_CLAIM_DEF_FORMATTED_REG_EX,
        INIT_ATTR_REPO_FORMATTED_REG_EX,
        ADD_ATTRS_FORMATTED_REG_EX,
        SHOW_LINK_FORMATTED_REG_EX,
        SHOW_FILE_FORMATTED_REG_EX,
        LOAD_FILE_FORMATTED_REG_EX,
        ADD_ATTRS_PROVER_FORMATTED_REG_EX,
        CONNECT_FORMATTED_REG_EX,
        DISCONNECT_FORMATTED_REG_EX,
        SYNC_LINK_FORMATTED_REG_EX,
        ACCEPT_LINK_FORMATTED_REG_EX,
        # SHOW_CLAIM_REQ_FORMATTED_REG_EX,
        SHOW_PROOF_REQ_FORMATTED_REG_EX,
        SHOW_CLAIM_FORMATTED_REG_EX,
        LIST_CLAIMS_FORMATTED_REG_EX,
        LIST_LINKS_FORMATTED_REG_EX,
        REQUEST_CLAIM_FORMATTED_REG_EX,
        SET_ATTRIBUTE_FORMATTED_REG_EX,
        PING_TARGET_FORMATTED_REG_EX,
        SEND_PROOF_FORMATTED_REG_EX,
        SEND_NODE_FORMATTED_REG_EX,
        SEND_POOL_UPG_FORMATTED_REG_EX,
        SEND_POOL_CONFIG_FORMATTED_REG_EX,
        REQ_AVAIL_CLAIMS_FORMATTED_REG_EX,
        NEW_ID_FORMATTED_REG_EX,
        SEND_PROOF_REQ_FORMATTED_REG_EX,
        REQ_AVAIL_CLAIMS_FORMATTED_REG_EX,
        CHANGE_CURRENT_KEY_FORMATTED_REG_EX
    ]


NEXT_COMMANDS_TO_TRY_TEXT = "Try Next:"
USAGE_TEXT = "Usage:"
