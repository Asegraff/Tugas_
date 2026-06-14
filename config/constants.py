"""Application Constants"""

# Rigs
RIGS = {
    '18': {'name': 'RIG 18', 'client': 'PT ABC'},
    '29': {'name': 'RIG 29', 'client': 'PT DEF'},
    '60': {'name': 'RIG 60', 'client': 'PT GHI'},
    '61': {'name': 'RIG 61', 'client': 'PT JKL'},
    '82': {'name': 'RIG 82', 'client': 'PT MNO'},
    '87': {'name': 'RIG 87', 'client': 'PT PQR'},
    '89': {'name': 'RIG 89', 'client': 'PT STU'},
    '90': {'name': 'RIG 90', 'client': 'PT VWX'},
    '92': {'name': 'RIG 92', 'client': 'PT YZA'},
    '94': {'name': 'RIG 94', 'client': 'PT BCD'},
}

# Categories
CATEGORIES = {
    'DSR': {'name': 'Daily Safety Report', 'code': 'DSR'},
    'VISITOR': {'name': 'Visitor', 'code': 'VISITOR'},
    'WSR': {'name': 'Weekly Safety Report', 'code': 'WSR'},
    'SERCO': {'name': 'Service Company', 'code': 'SERCO'},
    'NDT': {'name': 'Non-Destructive Test', 'code': 'NDT'},
    'SEMBAKO': {'name': 'Sembako', 'code': 'SEMBAKO'},
}

# User Roles
ROLES = {
    'ADMIN': 'Administrator',
    'SUPERVISOR': 'Supervisor',
    'OPERATOR': 'Operator',
    'VIEWER': 'Viewer',
}

# Invoice Status
INVOICE_STATUS = {
    'DRAFT': 'Draft',
    'PENDING': 'Pending',
    'APPROVED': 'Approved',
    'SENT': 'Sent',
    'PAID': 'Paid',
    'CANCELLED': 'Cancelled',
}

# Transaction Types
TRANSACTION_TYPES = {
    'INCOME': 'Income',
    'EXPENSE': 'Expense',
    'SERVICE': 'Service',
}

# Sheet Names in Excel
EXCEL_SHEETS = {
    'DASHBOARD': 'Dashboard',
    'INPUT_TRANSAKSI': 'InputTransaksi',
    'MASTER_RIG': 'MasterRig',
    'MASTER_KATEGORI': 'MasterKategori',
    'DATA_TRANSAKSI': 'DataTransaksi',
    'INVOICE_GENERATOR': 'InvoiceGenerator',
    'SETTING': 'Setting',
    'LOG': 'Log',
}
