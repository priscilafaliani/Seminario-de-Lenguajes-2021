categorias = """Adaptive Technologies
Artistic Software
Communications

    BBS
    Chat
        ICQ
        Internet Relay Chat
        Unix Talk 
    Conferencing
    Email
        Address Book
        Email Clients (MUA)
        Filters
        Mail Transport Agents
        Mailing List Servers
        Post-Office
            IMAP
            POP3 
    FIDO
    Fax
    File Sharing
        Gnutella 
    Ham Radio
    Internet Phone
    Telephony
    Usenet News 

Database

    Database Engines/Servers
    Front-Ends 

Desktop Environment

    File Managers
    GNUstep
    Gnome
    K Desktop Environment (KDE)
    Screen Savers
    Window Managers
        Blackbox
        Fluxbox
        XFCE 

Documentation

    Sphinx 

Education

    Computer Aided Instruction (CAI)
    Testing 

Games/Entertainment

    Arcade
    Board Games
    First Person Shooters
    Fortune Cookies
    Multi-User Dungeons (MUD)
    Puzzle Games
    Real Time Strategy
    Role-Playing
    Side-Scrolling/Arcade Games
    Simulation
    Turn Based Strategy 

Home Automation
Internet

    File Transfer Protocol (FTP)
    Finger
    Log Analysis
    Name Service (DNS)
    Proxy Servers
    WAP
    WWW/HTTP
        Browsers
        Dynamic Content
            CGI Tools/Libraries
            Content Management System
            Message Boards
            News/Diary
            Page Counters
            Wiki 
        HTTP Servers
        Indexing/Search
        Session
        Site Management
            Link Checking 
        WSGI
            Application
            Middleware
            Server 
    XMPP
    Z39.50 

Multimedia

    Graphics
        3D Modeling
        3D Rendering
        Capture
            Digital Camera
            Scanners
            Screen Capture 
        Editors
            Raster-Based
            Vector-Based 
        Graphics Conversion
        Presentation
        Viewers 
    Sound/Audio
        Analysis
        CD Audio
            CD Playing
            CD Ripping
            CD Writing 
        Capture/Recording
        Conversion
        Editors
        MIDI
        Mixers
        Players
            MP3 
        Sound Synthesis
        Speech 
    Video
        Capture
        Conversion
        Display
        Non-Linear Editor 

Office/Business

    Financial
        Accounting
        Investment
        Point-Of-Sale
        Spreadsheet 
    Groupware
    News/Diary
    Office Suites
    Scheduling 

Other/Nonlisted Topic
Printing
Religion
Scientific/Engineering

    Artificial Intelligence
    Artificial Life
    Astronomy
    Atmospheric Science
    Bio-Informatics
    Chemistry
    Electronic Design Automation (EDA)
    GIS
    Human Machine Interfaces
    Hydrology
    Image Processing
    Image Recognition
    Information Analysis
    Interface Engine/Protocol Translator
    Mathematics
    Medical Science Apps.
    Physics
    Visualization 

Security

    Cryptography 

Sociology

    Genealogy
    History 

Software Development

    Assemblers
    Bug Tracking
    Build Tools
    Code Generators
    Compilers
    Debuggers
    Disassemblers
    Documentation
    Embedded Systems
    Internationalization
    Interpreters
    Libraries
        Application Frameworks
        Java Libraries
        PHP Classes
        Perl Modules
        Pike Modules
        Python Modules
        Ruby Modules
        Tcl Extensions
        pygame 
    Localization
    Object Brokering
        CORBA 
    Pre-processors
    Quality Assurance
    Testing
        Acceptance
        BDD
        Mocking
        Traffic Generation
        Unit 
    User Interfaces
    Version Control
        Bazaar
        CVS
        Git
        Mercurial
        RCS
        SCCS 
    Widget Sets 

System

    Archiving
        Backup
        Compression
        Mirroring
        Packaging 
    Benchmark
    Boot
        Init 
    Clustering
    Console Fonts
    Distributed Computing
    Emulators
    Filesystems
    Hardware
        Hardware Drivers
        Mainframes
        Symmetric Multi-processing
        Universal Serial Bus (USB) 
    Installation/Setup
    Logging
    Monitoring
    Networking
        Firewalls
        Monitoring
            Hardware Watchdog 
        Time Synchronization 
    Operating System
    Operating System Kernels
        BSD
        GNU Hurd
        Linux 
    Power (UPS)
    Recovery Tools
    Shells
    Software Distribution
    System Shells
    Systems Administration
        Authentication/Directory
            LDAP
            NIS 

Terminals

    Serial
    Telnet
    Terminal Emulators/X Terminals 

Text Editors

    Documentation
    Emacs
    Integrated Development Environments (IDE)
    Text Processing
    Word Processors 

Text Processing

    Filters
    Fonts
    General
    Indexing
    Linguistic
    Markup
        HTML
        LaTeX
        Markdown
        SGML
        VRML
        XML
        reStructuredText 

Utilities
"""


# output
"""
[
    {'nombre': 'Adaptive Technologies', 'subcategorias': []}, 
    {'nombre': 'Artistic Software', 'subcategorias': []}, 
    {'nombre': 'Communications', 'subcategorias': [
        {'nombre': '    BBS', 'subcategorias': []}, 
        {'nombre': '    Chat', 'subcategorias': [
            {'nombre': '        ICQ', 'subcategorias': []}, 
            {'nombre': '        Internet Relay Chat', 'subcategorias': []}, 
            {'nombre': '        Unix Talk ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Conferencing', 'subcategorias': []}, 
        {'nombre': '    Email', 'subcategorias': [
            {'nombre': '        Address Book', 'subcategorias': []}, 
            {'nombre': '        Email Clients (MUA)', 'subcategorias': []}, 
            {'nombre': '        Filters', 'subcategorias': []}, 
            {'nombre': '        Mail Transport Agents', 'subcategorias': []}, 
            {'nombre': '        Mailing List Servers', 'subcategorias': []}, 
            {'nombre': '        Post-Office', 'subcategorias': [
                {'nombre': '            IMAP', 'subcategorias': []}, 
                {'nombre': '            POP3 ', 'subcategorias': []}
            ]}
        ]}, 
        {'nombre': '    FIDO', 'subcategorias': []}, 
        {'nombre': '    Fax', 'subcategorias': []}, 
        {'nombre': '    File Sharing', 'subcategorias': [
            {'nombre': '        Gnutella ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Ham Radio', 'subcategorias': []}, 
        {'nombre': '    Internet Phone', 'subcategorias': []}, 
        {'nombre': '    Telephony', 'subcategorias': []}, 
        {'nombre': '    Usenet News ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Database', 'subcategorias': [
        {'nombre': '    Database Engines/Servers', 'subcategorias': []}, 
        {'nombre': '    Front-Ends ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Desktop Environment', 'subcategorias': [
        {'nombre': '    File Managers', 'subcategorias': []}, 
        {'nombre': '    GNUstep', 'subcategorias': []}, 
        {'nombre': '    Gnome', 'subcategorias': []}, 
        {'nombre': '    K Desktop Environment (KDE)', 'subcategorias': []}, 
        {'nombre': '    Screen Savers', 'subcategorias': []}, 
        {'nombre': '    Window Managers', 'subcategorias': [
            {'nombre': '        Blackbox', 'subcategorias': []}, 
            {'nombre': '        Fluxbox', 'subcategorias': []}, 
            {'nombre': '        XFCE ', 'subcategorias': []}
        ]}
    ]}, 
    {'nombre': 'Documentation', 'subcategorias': [
        {'nombre': '    Sphinx ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Education', 'subcategorias': [
        {'nombre': '    Computer Aided Instruction (CAI)', 'subcategorias': []}, 
        {'nombre': '    Testing ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Games/Entertainment', 'subcategorias': [
        {'nombre': '    Arcade', 'subcategorias': []}, 
        {'nombre': '    Board Games', 'subcategorias': []}, 
        {'nombre': '    First Person Shooters', 'subcategorias': []}, 
        {'nombre': '    Fortune Cookies', 'subcategorias': []}, 
        {'nombre': '    Multi-User Dungeons (MUD)', 'subcategorias': []}, 
        {'nombre': '    Puzzle Games', 'subcategorias': []}, 
        {'nombre': '    Real Time Strategy', 'subcategorias': []}, 
        {'nombre': '    Role-Playing', 'subcategorias': []}, 
        {'nombre': '    Side-Scrolling/Arcade Games', 'subcategorias': []}, 
        {'nombre': '    Simulation', 'subcategorias': []}, 
        {'nombre': '    Turn Based Strategy ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Home Automation', 'subcategorias': []}, 
    {'nombre': 'Internet', 'subcategorias': [
        {'nombre': '    File Transfer Protocol (FTP)', 'subcategorias': []}, 
        {'nombre': '    Finger', 'subcategorias': []}, 
        {'nombre': '    Log Analysis', 'subcategorias': []}, 
        {'nombre': '    Name Service (DNS)', 'subcategorias': []}, 
        {'nombre': '    Proxy Servers', 'subcategorias': []}, 
        {'nombre': '    WAP', 'subcategorias': []}, 
        {'nombre': '    WWW/HTTP', 'subcategorias': [
            {'nombre': '        Browsers', 'subcategorias': []}, 
            {'nombre': '        Dynamic Content', 'subcategorias': [
                {'nombre': '            CGI Tools/Libraries', 'subcategorias': []}, 
                {'nombre': '            Content Management System', 'subcategorias': []}, 
                {'nombre': '            Message Boards', 'subcategorias': []}, 
                {'nombre': '            News/Diary', 'subcategorias': []}, 
                {'nombre': '            Page Counters', 'subcategorias': []}, 
                {'nombre': '            Wiki ', 'subcategorias': []}
            ]}, 
            {'nombre': '        HTTP Servers', 'subcategorias': []},
            {'nombre': '        Indexing/Search', 'subcategorias': []}, 
            {'nombre': '        Session', 'subcategorias': []}, 
            {'nombre': '        Site Management', 'subcategorias': [
                {'nombre': '            Link Checking ', 'subcategorias': []}
            ]}, 
            {'nombre': '        WSGI', 'subcategorias': [
                {'nombre': '            Application', 'subcategorias': []}, 
                {'nombre': '            Middleware', 'subcategorias': []}, 
                {'nombre': '            Server ', 'subcategorias': []}
            ]}
        ]}, 
        {'nombre': '    XMPP', 'subcategorias': []}, 
        {'nombre': '    Z39.50 ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Multimedia', 'subcategorias': [
        {'nombre': '    Graphics', 'subcategorias': [
            {'nombre': '        3D Modeling', 'subcategorias': []}, 
            {'nombre': '        3D Rendering', 'subcategorias': []}, 
            {'nombre': '        Capture', 'subcategorias': [
                {'nombre': '            Digital Camera', 'subcategorias': []}, 
                {'nombre': '                Scanners', 'subcategorias': []}, 
                {'nombre': '            Screen Capture ', 'subcategorias': []}
            ]}, 
            {'nombre': '        Editors', 'subcategorias': [
                {'nombre': '            Raster-Based', 'subcategorias': []}, 
                {'nombre': '            Vector-Based ', 'subcategorias': []}
                ]}, {'nombre': '        Graphics Conversion', 'subcategorias': []}, 
                {'nombre': '        Presentation', 'subcategorias': []}, 
                {'nombre': '        Viewers ', 'subcategorias': []}
            ]}, 
            {'nombre': '    Sound/Audio', 'subcategorias': [
                {'nombre': '        Analysis', 'subcategorias': []}, 
                {'nombre': '        CD Audio', 'subcategorias': [
                    {'nombre': '            CD Playing', 'subcategorias': []}, 
                    {'nombre': '            CD Ripping', 'subcategorias': []}, 
                    {'nombre': '            CD Writing ', 'subcategorias': []}
                ]}, 
                {'nombre': '        Capture/Recording', 'subcategorias': []}, 
                {'nombre': '        Conversion', 'subcategorias': []}, 
                {'nombre': '        Editors', 'subcategorias': []}, 
                {'nombre': '        MIDI', 'subcategorias': []}, 
                {'nombre': '        Mixers', 'subcategorias': []}, 
                {'nombre': '        Players', 'subcategorias': [
                    {'nombre': '            MP3 ', 'subcategorias': []}
                ]}, 
                {'nombre': '        Sound Synthesis', 'subcategorias': []}, 
                {'nombre': '        Speech ', 'subcategorias': []}
            ]}, 
            {'nombre': '    Video', 'subcategorias': [
                {'nombre': '        Capture', 'subcategorias': []}, 
                {'nombre': '        Conversion', 'subcategorias': []}, 
                {'nombre': '        Display', 'subcategorias': []}, 
                {'nombre': '        Non-Linear Editor ', 'subcategorias': []}
            ]}
    ]}, 
    {'nombre': 'Office/Business', 'subcategorias': [
        {'nombre': '    Financial', 'subcategorias': [
            {'nombre': '        Accounting', 'subcategorias': []}, 
            {'nombre': '        Investment', 'subcategorias': []}, 
            {'nombre': '        Point-Of-Sale', 'subcategorias': []}, 
            {'nombre': '        Spreadsheet ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Groupware', 'subcategorias': []}, 
        {'nombre': '    News/Diary', 'subcategorias': []}, 
        {'nombre': '    Office Suites', 'subcategorias': []}, 
        {'nombre': '    Scheduling ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Other/Nonlisted Topic', 'subcategorias': []}, 
    {'nombre': 'Printing', 'subcategorias': []}, 
    {'nombre': 'Religion', 'subcategorias': []}, 
    {'nombre': 'Scientific/Engineering', 'subcategorias': [
        {'nombre': '    Artificial Intelligence', 'subcategorias': []}, 
        {'nombre': '    Artificial Life', 'subcategorias': []}, 
        {'nombre': '    Astronomy', 'subcategorias': []}, 
        {'nombre': '    Atmospheric Science', 'subcategorias': []}, 
        {'nombre': '    Bio-Informatics', 'subcategorias': []}, 
        {'nombre': '    Chemistry', 'subcategorias': []}, 
        {'nombre': '    Electronic Design Automation (EDA)', 'subcategorias': []}, 
        {'nombre': '    GIS', 'subcategorias': []}, 
        {'nombre': '    Human Machine Interfaces', 'subcategorias': []}, 
        {'nombre': '    Hydrology', 'subcategorias': []}, 
        {'nombre': '    Image Processing', 'subcategorias': []}, 
        {'nombre': '    Image Recognition', 'subcategorias': []}, 
        {'nombre': '    Information Analysis', 'subcategorias': []}, 
        {'nombre': '    Interface Engine/Protocol Translator', 'subcategorias': []}, 
        {'nombre': '    Mathematics', 'subcategorias': []}, 
        {'nombre': '    Medical Science Apps.', 'subcategorias': []}, 
        {'nombre': '    Physics', 'subcategorias': []}, 
        {'nombre': '    Visualization ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Security', 'subcategorias': [
        {'nombre': '    Cryptography ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Sociology', 'subcategorias': [
        {'nombre': '    Genealogy', 'subcategorias': []}, 
        {'nombre': '    History ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Software Development', 'subcategorias': [
        {'nombre': '    Assemblers', 'subcategorias': []}, 
        {'nombre': '    Bug Tracking', 'subcategorias': []}, 
        {'nombre': '    Build Tools', 'subcategorias': []}, 
        {'nombre': '    Code Generators', 'subcategorias': []}, 
        {'nombre': '    Compilers', 'subcategorias': []}, 
        {'nombre': '    Debuggers', 'subcategorias': []}, 
        {'nombre': '    Disassemblers', 'subcategorias': []}, 
        {'nombre': '    Documentation', 'subcategorias': []}, 
        {'nombre': '    Embedded Systems', 'subcategorias': []}, 
        {'nombre': '    Internationalization', 'subcategorias': []}, 
        {'nombre': '    Interpreters', 'subcategorias': []}, 
        {'nombre': '    Libraries', 'subcategorias': [
            {'nombre': '        Application Frameworks', 'subcategorias': []}, 
            {'nombre': '        Java Libraries', 'subcategorias': []}, 
            {'nombre': '        PHP Classes', 'subcategorias': []}, 
            {'nombre': '        Perl Modules', 'subcategorias': []}, 
            {'nombre': '        Pike Modules', 'subcategorias': []}, 
            {'nombre': '        Python Modules', 'subcategorias': []}, 
            {'nombre': '        Ruby Modules', 'subcategorias': []}, 
            {'nombre': '        Tcl Extensions', 'subcategorias': []}, 
            {'nombre': '        pygame ', 'subcategorias': []}]}, 
            {'nombre': '    Localization', 'subcategorias': []}, 
            {'nombre': '    Object Brokering', 'subcategorias': [
                {'nombre': '        CORBA ', 'subcategorias': []}
            ]}, 
            {'nombre': '    Pre-processors', 'subcategorias': []}, 
            {'nombre': '    Quality Assurance', 'subcategorias': []}, 
            {'nombre': '    Testing', 'subcategorias': [
                {'nombre': '        Acceptance', 'subcategorias': []}, 
                {'nombre': '        BDD', 'subcategorias': []}, 
                {'nombre': '        Mocking', 'subcategorias': []}, 
                {'nombre': '        Traffic Generation', 'subcategorias': []}, 
                {'nombre': '        Unit ', 'subcategorias': []}
            ]}, 
            {'nombre': '    User Interfaces', 'subcategorias': []}, 
            {'nombre': '    Version Control', 'subcategorias': [
                {'nombre': '        Bazaar', 'subcategorias': []}, 
                {'nombre': '        CVS', 'subcategorias': []}, 
                {'nombre': '        Git', 'subcategorias': []}, 
                {'nombre': '        Mercurial', 'subcategorias': []}, 
                {'nombre': '        RCS', 'subcategorias': []}, 
                {'nombre': '        SCCS ', 'subcategorias': []}
            ]}, 
            {'nombre': '    Widget Sets ', 'subcategorias': []}
    ]}, 
    {'nombre': 'System', 'subcategorias': [
        {'nombre': '    Archiving', 'subcategorias': [
            {'nombre': '        Backup', 'subcategorias': []}, 
            {'nombre': '        Compression', 'subcategorias': []}, 
            {'nombre': '        Mirroring', 'subcategorias': []}, 
            {'nombre': '        Packaging ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Benchmark', 'subcategorias': []}, 
        {'nombre': '    Boot', 'subcategorias': [
            {'nombre': '        Init ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Clustering', 'subcategorias': []}, 
        {'nombre': '    Console Fonts', 'subcategorias': []}, 
        {'nombre': '    Distributed Computing', 'subcategorias': []}, 
        {'nombre': '    Emulators', 'subcategorias': []}, 
        {'nombre': '    Filesystems', 'subcategorias': []}, 
        {'nombre': '    Hardware', 'subcategorias': [
            {'nombre': '        Hardware Drivers', 'subcategorias': []}, 
            {'nombre': '        Mainframes', 'subcategorias': []}, 
            {'nombre': '        Symmetric Multi-processing', 'subcategorias': []}, 
            {'nombre': '        Universal Serial Bus (USB) ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Installation/Setup', 'subcategorias': []}, 
        {'nombre': '    Logging', 'subcategorias': []}, 
        {'nombre': '    Monitoring', 'subcategorias': []}, 
        {'nombre': '    Networking', 'subcategorias': [
            {'nombre': '        Firewalls', 'subcategorias': []}, 
            {'nombre': '        Monitoring', 'subcategorias': [
                {'nombre': '            Hardware Watchdog ', 'subcategorias': []}
            ]}, 
            {'nombre': '        Time Synchronization ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Operating System', 'subcategorias': []}, 
        {'nombre': '    Operating System Kernels', 'subcategorias': [
            {'nombre': '        BSD', 'subcategorias': []}, 
            {'nombre': '        GNU Hurd', 'subcategorias': []}, 
            {'nombre': '        Linux ', 'subcategorias': []}
        ]}, 
        {'nombre': '    Power (UPS)', 'subcategorias': []}, 
        {'nombre': '    Recovery Tools', 'subcategorias': []}, 
        {'nombre': '    Shells', 'subcategorias': []}, 
        {'nombre': '    Software Distribution', 'subcategorias': []}, 
        {'nombre': '    System Shells', 'subcategorias': []},
        {'nombre': '    Systems Administration', 'subcategorias': [
            {'nombre': '        Authentication/Directory', 'subcategorias': [
                {'nombre': '            LDAP', 'subcategorias': []}, 
                {'nombre': '            NIS ', 'subcategorias': []}
            ]}
        ]}
    ]}, 
    {'nombre': 'Terminals', 'subcategorias': [
        {'nombre': '    Serial', 'subcategorias': []}, 
        {'nombre': '    Telnet', 'subcategorias': []}, 
        {'nombre': '    Terminal Emulators/X Terminals ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Text Editors', 'subcategorias': [
        {'nombre': '    Documentation', 'subcategorias': []}, 
        {'nombre': '    Emacs', 'subcategorias': []}, 
        {'nombre': '    Integrated Development Environments (IDE)', 'subcategorias': []}, 
        {'nombre': '    Text Processing', 'subcategorias': []}, 
    {'nombre': '    Word Processors ', 'subcategorias': []}
    ]}, 
    {'nombre': 'Text Processing', 'subcategorias': [
        {'nombre': '    Filters', 'subcategorias': []}, 
        {'nombre': '    Fonts', 'subcategorias': []}, 
        {'nombre': '    General', 'subcategorias': []}, 
        {'nombre': '    Indexing', 'subcategorias': []}, 
        {'nombre': '    Linguistic', 'subcategorias': []},
         {'nombre': '   Markup', 'subcategorias': [
             {'nombre': '        HTML', 'subcategorias': []}, 
             {'nombre': '        LaTeX', 'subcategorias': []}, 
             {'nombre': '        Markdown', 'subcategorias': []}, 
             {'nombre': '        SGML', 'subcategorias': []}, 
             {'nombre': '        VRML', 'subcategorias': []}, 
             {'nombre': '        XML', 'subcategorias': []}, 
             {'nombre': '        reStructuredText ', 'subcategorias': []}
        ]}
    ]}, 
    {'nombre': 'Utilities', 'subcategorias': []}
]
"""