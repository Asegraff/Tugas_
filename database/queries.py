"""Database Queries Module"""

class DatabaseQueries:
    """SQL Query templates"""
    
    # Master Rig Queries
    GET_ALL_RIGS = "SELECT * FROM MasterRig ORDER BY ID_Rig"
    GET_RIG_BY_ID = "SELECT * FROM MasterRig WHERE ID_Rig = ?"
    INSERT_RIG = "INSERT INTO MasterRig (ID_Rig, NamaRig, Client) VALUES (?, ?, ?)"
    UPDATE_RIG = "UPDATE MasterRig SET NamaRig = ?, Client = ? WHERE ID_Rig = ?"
    DELETE_RIG = "DELETE FROM MasterRig WHERE ID_Rig = ?"
    
    # Master Kategori Queries
    GET_ALL_CATEGORIES = "SELECT * FROM MasterKategori ORDER BY ID_Kategori"
    GET_CATEGORY_BY_ID = "SELECT * FROM MasterKategori WHERE ID_Kategori = ?"
    INSERT_CATEGORY = "INSERT INTO MasterKategori (ID_Kategori, NamaKategori) VALUES (?, ?)"
    UPDATE_CATEGORY = "UPDATE MasterKategori SET NamaKategori = ? WHERE ID_Kategori = ?"
    DELETE_CATEGORY = "DELETE FROM MasterKategori WHERE ID_Kategori = ?"
    
    # Transaksi Harian Queries
    GET_ALL_TRANSACTIONS = "SELECT * FROM TransaksiHarian ORDER BY Tanggal DESC"
    GET_TRANSACTIONS_BY_PERIOD = """
        SELECT * FROM TransaksiHarian 
        WHERE Tanggal >= ? AND Tanggal <= ? 
        ORDER BY Tanggal DESC
    """
    GET_TRANSACTIONS_BY_RIG = """
        SELECT * FROM TransaksiHarian 
        WHERE Rig = ? 
        ORDER BY Tanggal DESC
    """
    INSERT_TRANSACTION = """
        INSERT INTO TransaksiHarian (Tanggal, Rig, Kategori, Qty_Pax, Harga, Total)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    UPDATE_TRANSACTION = """
        UPDATE TransaksiHarian 
        SET Tanggal = ?, Rig = ?, Kategori = ?, Qty_Pax = ?, Harga = ?, Total = ?
        WHERE ID = ?
    """
    DELETE_TRANSACTION = "DELETE FROM TransaksiHarian WHERE ID = ?"
    
    # Invoice Queries
    GET_ALL_INVOICES = "SELECT * FROM Invoice ORDER BY Periode DESC"
    GET_INVOICE_BY_PERIOD = """
        SELECT * FROM Invoice 
        WHERE Periode = ? 
        ORDER BY Rig
    """
    GET_INVOICE_BY_RIG_PERIOD = """
        SELECT * FROM Invoice 
        WHERE Rig = ? AND Periode = ?
    """
    INSERT_INVOICE = """
        INSERT INTO Invoice (NoInvoice, Rig, Periode, NilaiInvoice, Status, CreatedDate)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    UPDATE_INVOICE = """
        UPDATE Invoice 
        SET NilaiInvoice = ?, Status = ?, UpdatedDate = ?
        WHERE ID_Invoice = ?
    """
    DELETE_INVOICE = "DELETE FROM Invoice WHERE ID_Invoice = ?"
    
    # User Login Queries
    GET_ALL_USERS = "SELECT * FROM UserLogin ORDER BY Username"
    GET_USER_BY_USERNAME = "SELECT * FROM UserLogin WHERE Username = ?"
    INSERT_USER = """
        INSERT INTO UserLogin (Username, Password, Role, CreatedDate)
        VALUES (?, ?, ?, ?)
    """
    UPDATE_USER = """
        UPDATE UserLogin 
        SET Password = ?, Role = ?, UpdatedDate = ?
        WHERE ID_User = ?
    """
    DELETE_USER = "DELETE FROM UserLogin WHERE ID_User = ?"
    
    # Summary Queries
    GET_SUMMARY_BY_RIG_PERIOD = """
        SELECT 
            Rig,
            Kategori,
            SUM(Qty_Pax) as Total_Qty,
            SUM(Total) as Total_Amount
        FROM TransaksiHarian
        WHERE Tanggal >= ? AND Tanggal <= ?
        GROUP BY Rig, Kategori
        ORDER BY Rig, Kategori
    """
    
    GET_SUMMARY_BY_RIG = """
        SELECT 
            Rig,
            SUM(Qty_Pax) as Total_Qty,
            SUM(Total) as Total_Amount
        FROM TransaksiHarian
        WHERE Tanggal >= ? AND Tanggal <= ?
        GROUP BY Rig
        ORDER BY Rig
    """
