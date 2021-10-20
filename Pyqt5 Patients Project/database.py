from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createPatientsTable():
    """Create the Patients table in the database."""

# Creating an instance of QSqlQuery class
# To be able to create navigate and retrieve data from SQL queries
    query = QSqlQuery()

    return query.exec(
    """
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        phone_number INT,
        email VARCHAR(40),
        amka INT,
        address VARCHAR(40),
        illness VARCHAR(1000)
    )
    """
    )

def _createUsersTable():
    """ Create Users table in patients database.sqlite """

    query = QSqlQuery()

    return query.exec(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        username varchar(40) NOT NULL,
        password varchar(40) NOT NULL
        )
    """
    )

def _createTestsTable():
    """ Create tests table in patients database.sqlite """

    query = QSqlQuery()

    return query.exec(
    """
    CREATE TABLE IF NOT EXISTS allergy_tests (
        test_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        test_name varchar(40) NOT NULL
        )
    """
    )

def _populateTestsTable():
    query = QSqlQuery()

    testslist = ["Ακακία (Acacia Dealbata )", "Κυπαρίσι (Cypressus Sempervirens) ","Λεύκα (Populus Alba)", "Ιτιά(salix Nigra) ",
                    "Πλάτανος (Platanus Vulgaris)","Πεύκο (Pinus Sylvestris)","Ελιά (Olive Europa)","Μουριά (Morus Alba)",
                    "Μιμόζα (Mimosa)","Μείγμα Αγρωστωδών (Mixed Grasses) ","Αγριάδα (Cynodon Dactylon",
                    "Φλέως ο Λειμώνιος (phleum Pratensis)","Καλαμπόκι","Σιτάρι",
                    "Βρώμη","Σίκαλη","Περδικάκι (Parietaria officinalis)","Χηνοπόδιο","Πεντάνευρο","Λάπαθο","Πικροράδικο",
                    "Χρυσάνθεμο","Αρτεμησία(Αψιθιά)","Ξινήθρα",
                    "Μείγμα Ζιζανίων","ΑlternariaTenuis","Cladosporium Herbarum","Aspergillus Fumigatus",
                    "Penicillium Notatum","Penicillium Notatum","Mucor","Fusarium Oxysporum",
                    "Mείγμα μυκήτων","Derm.Pteronyssinus","Derm.Farinae","Γάτα","Σκύλος", "Κρόκος αυγού", "Λεύκωμα αυγού","Γάλα Κατσίκας",
                    "Β-λακτοσφαιρίνη","Α-λακταλβουμίνη","Καζεΐνη",
                    "Κρέας χοιρινού","Κρέας αρνιού","Κρέας μοσχαριού","Κρέας κοτόπουλου","Μύδια","Στρείδια","Γαρίδες","Τόνος",
                    "Σολωμός","Ροδάκινο","Φράουλα","Ακτινίδιο","Μπανάνα","Σαρδελλα","Βακαλάος","Σόγια","Μήλο","Πορτοκάλι",
                    "Αμύγδαλο","Καρύδι","Φουντούκι","Φιστίκι","Αλεύρι σιταριού","Αλεύρι κριθαριού","Αλεύρι σίκαλης","Αλεύρι βρώμης",
                    "Σέλινο","Τομάτα","Σπανάκι","Καλαμπόκι","Κακάο","Βύνη","Φιστίκι","Πάπρικα","Ισταμινη","Control","Σουσάμι"]


    for test in testslist:
        query.prepare("INSERT INTO allergy_tests (test_name)" "VALUES (:test_name)")
        query.bindValue(":test_name", test)
        query.exec_()
     

def _createTestsDoneTable():
    """ Create testsdone table in patients database.sqlite """

    query = QSqlQuery()

    return query.exec(
    """
    CREATE TABLE IF NOT EXISTS tests_done (
        test_done_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        datetime_int INT NOT NULL,
        allergy_test_id INTEGER NOT NULL,
        patient_id INTEGER NOT NULL,
        allergy_grade REAL DEFAULT 0,
        FOREIGN KEY(patient_id) REFERENCES patients(id),
        FOREIGN KEY(allergy_test_id) REFERENCES allergy_tests(test_id)   
        )
    """
    ) 

def createConnection(databaseName):
    """Create and open a database connection."""

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warrning(None, "Patients", f"Database error :{connection.lastError().text()}")
        return False

    _createPatientsTable()
    _createUsersTable()
    _createTestsTable()
    _createTestsDoneTable()

    # only run this once to poulate the tests into the database
    # Maybe we could check if its empy and then run it
    # _populateTestsTable()
    
    return True
