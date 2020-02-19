ERROR_CODES = {
    0: 'Success',
    1: 'Insufficient Funds',
    2: 'Less Than Minimum Transaction Value',
    3: 'More Than Maximum Transaction Value',
    4: 'Would Exceed Daily Transfer Limit',
    5: 'Would Exceed Minimum Balance',
    6: 'Unresolved Primary Party',
    7: 'Unresolved Receiver Party',
    8: 'Would Exceed Maximum Balance',
    11: 'Debit Account Invalid',
    12: 'Credit Account Invalid',
    13: 'Unresolved Debit Account',
    14: 'Unresolved Credit Account',
    15: 'Duplicate Detected',
    17: 'Internal Failure',
    20: 'Unresolved Initiator',
    26: 'Traffic blocking condition in place',
}

IDENTIFIER_TYPES = {
    1: 'MSISDN',
    2: 'Till Number',
    4: 'Shortcode'
}

CLIENT_RESPONSE_CODES = {
    '0': 'Success (for C2B)',
    '00000000': 'Success (For APIs that are not C2B)',
}
