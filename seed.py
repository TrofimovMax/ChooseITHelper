# seed.py

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models.framework import Framework
from models.language import Language

"""
List of websites with information about programming languages
https://medium.com/web-development-zone/a-complete-list-of-computer-programming-languages-1d8bc5a891f
https://en.wikipedia.org/wiki/List_of_relational_database_management_systems
https://en.wikipedia.org/wiki/NoSQL
"""

technologies_data = [
    # Interpreted
    # An interpreted language is a programming language for which most of its implementations execute instructions
    # directly, without previously compiling a program into machine-language instructions.
    # The interpreter executes the program directly, translating each statement into a sequence of one or more
    # subroutines already compiled into machine code. (Wikipedia)

    {
        "language": "APL",
        "frameworks": [
            {
                "name": "Dyalog",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "NARS2000",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Sharp APL",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "APL2",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "J",
                "application_area": "DATA_SCIENCE"
            },
        ]
    },
    {
        "language": "AutoIt",
        "frameworks": [
            {
                "name": "AutoItX",
                "application_area": "AUTOMATION"
            },
            {
                "name": "Selenium",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "AviCode",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "AutoHotkey",
                "application_area": "AUTOMATION"
            },
            {
                "name": "WinAutomation",
                "application_area": "BUSINESS_SYSTEMS"
            },
        ]
    },
    {
        "language": "BASIC",
        "frameworks": [
            {
                "name": "FreeBASIC",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "QB64",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "PureBasic",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "VBScript",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Just BASIC",
                "application_area": "GENERAL_PURPOSE"
            },
        ]
    },
    {
        "language": "Eiffel",
        "frameworks": [
            {
                "name": "EiffelStudio",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "AutoProof",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "GOBO",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Esprit",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "SCOOP",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "Forth",
        "frameworks": [
            {
                "name": "SwiftForth",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "gforth",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "SP-Forth",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "4th Dimension",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "AmForth",
                "application_area": "EMBEDDED_SYSTEMS"
            }
        ]
    },
    {
        "language": "Frink",
        "frameworks": [
            {
                "name": "Frink Interpreter",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Frink Web Version",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Frink Physics API",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "NumPy",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "SciPy",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Game Maker Language",
        "frameworks": [
            {
                "name": "GameMaker Studio",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "GMEdit",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "GMLive",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "YoYoCompiler",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "Extension GML",
                "application_area": "GAME_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "ICI",
        "frameworks": [
            {
                "name": "ICI Standard Library",
                "application_area": "SCRIPTING"
            },
            {
                "name": "ICI Interpreter",
                "application_area": "SCRIPTING"
            },
            {
                "name": "ICIModule",
                "application_area": "SCRIPTING"
            },
            {
                "name": "Tcl/Tk",
                "application_area": "SCRIPTING"
            },
            {
                "name": "Boost",
                "application_area": "SCRIPTING"
            }
        ]
    },
    {
        "language": "J",
        "frameworks": [
            {
                "name": "J Software",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Jupyter J Kernel",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "J Playground",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "NumPy",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "SciPy",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Lisp",
        "frameworks": [
            {
                "name": "Common Lisp",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "SBCL",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Clojure",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Emacs Lisp",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Guile",
                "application_area": "SCRIPTING"
            }
        ]
    },
    {
        "language": "Lua",
        "frameworks": [
            {
                "name": "LÖVE",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "Corona SDK",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "OpenResty",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Tarantool",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Orbit",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "M",
        "frameworks": [
            {
                "name": "InterSystems Caché",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "MUMPS VistA",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "GT.M",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "YottaDB",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "OpenMRS",
                "application_area": "BUSINESS_SYSTEMS"
            }
        ]
    },
    {
        "language": "Python",
        "frameworks": [
            {
                "name": "Django",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Flask",
                "application_area": "WEB_DEVELOPMENT"
            },
        ]
    },
    {
        "language": "Pascal",
        "frameworks": [
            {
                "name": "Free Pascal",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Delphi",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Lazarus",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Turbo Pascal",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "PascalABC.NET",
                "application_area": "SYSTEMS_PROGRAMMING"
            }
        ]
    },
    {
        "language": "PCASTL",
        "frameworks": []
    },
    {
        "language": "Perl",
        "frameworks": [
            {
                "name": "Dancer",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Catalyst",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Mojolicious",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Plack",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Perl DBI",
                "application_area": "SCRIPTING"
            }
        ]
    },
    {
        "language": "PostScript",
        "frameworks": [
            {
                "name": "Ghostscript",
                "application_area": "AUTOMATION"
            },
            {
                "name": "PSUtils",
                "application_area": "AUTOMATION"
            },
            {
                "name": "EPS",
                "application_area": "AUTOMATION"
            },
            {
                "name": "PostScript Viewer",
                "application_area": "AUTOMATION"
            },
            {
                "name": "Evince",
                "application_area": "AUTOMATION"
            }
        ]
    },
    {
        "language": "REXX",
        "frameworks": [
            {
                "name": "ooRexx",
                "application_area": "SCRIPTING"
            },
            {
                "name": "Regina",
                "application_area": "SCRIPTING"
            },
            {
                "name": "BSF4ooRexx",
                "application_area": "SCRIPTING"
            },
            {
                "name": "NetRexx",
                "application_area": "SCRIPTING"
            },
            {
                "name": "KEXX",
                "application_area": "SCRIPTING"
            }
        ]
    },
    {
        "language": "Ruby",
        "frameworks": [
            {
                "name": "Ruby on Rails",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Sinatra",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Hanami",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Padrino",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Grape",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "S-Lang",
        "frameworks": [
            {
                "name": "S-Lang Interpreter",
                "application_area": "SCRIPTING"
            },
            {
                "name": "JED",
                "application_area": "SCRIPTING"
            },
            {
                "name": "Mutt",
                "application_area": "SCRIPTING"
            },
            {
                "name": "XPaint",
                "application_area": "SCRIPTING"
            },
            {
                "name": "XEphem",
                "application_area": "SCRIPTING"
            }
        ]
    },
    {
        "language": "Spin",
        "frameworks": [
            {
                "name": "Parallax IDE",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "SimpleIDE",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "Propeller GCC",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "Tachyon Forth",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "Propeller Tool",
                "application_area": "EMBEDDED_SYSTEMS"
            }
        ]
    },
    # Functional
    # Functional programming languages define every computation as a mathematical evaluation.
    # They focus on the application of functions. Many of the functional programming languages are bound to mathematical
    # calculations.
    {
        "language": "Charity",
        "frameworks": [
            {
                "name": "Haskell",
                "application_area": "MACHINE_LEARNING"
            },
            {
                "name": "Scala",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "ML",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Clean",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Idris",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "Clean",
        "frameworks": [
            {
                "name": "Clean IDE",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "CLEAN Libraries",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Clean I/O System",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "ObjectIO",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Haskell",
                "application_area": "MACHINE_LEARNING"
            }
        ]
    },
    {
        "language": "Curry",
        "frameworks": [
            {
                "name": "PAKCS",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "KiCS2",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Haskell",
                "application_area": "MACHINE_LEARNING"
            },
            {
                "name": "SWI-Prolog",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "MiniZinc",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Erlang",
        "frameworks": [
            {
                "name": "OTP",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Cowboy",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Ecto",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Phoenix",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Mnesia",
                "application_area": "BUSINESS_SYSTEMS"
            }
        ]
    },
    {
        "language": "F#",
        "frameworks": [
            {
                "name": "Fable",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "SAFE Stack",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Suave",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Giraffe",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Expecto",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Haskell",
        "frameworks": [
            {
                "name": "Yesod",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Scotty",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Snap",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Servant",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Hakyll",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "Joy",
        "frameworks": [
            {
                "name": "Haskell",
                "application_area": "MACHINE_LEARNING"
            },
            {
                "name": "ML",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Idris",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Forth",
                "application_area": "EMBEDDED_SYSTEMS"
            },
            {
                "name": "Factor",
                "application_area": "EMBEDDED_SYSTEMS"
            }
        ]
    },
    {
        "language": "Kite",
        "frameworks": [
            {
                "name": "Kite.js",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Node.js",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Express",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Koa",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Electron",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "ML",
        "frameworks": [
            {
                "name": "OCaml",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "SML",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "F#",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Coq",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Isabelle",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Nemerle",
        "frameworks": [
            {
                "name": "Nemerle Compiler",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": ".NET Framework",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Mono",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "SharpDevelop",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Visual Studio",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "OPAL",
        "frameworks": [
            {
                "name": "Eclipse IDE",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Jikes",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "OpenJDK",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Maven",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Gradle",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "OPS5",
        "frameworks": [
            {
                "name": "CLIPS",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Drools",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "Jess",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "Prolog",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "ILOG JRules",
                "application_area": "BUSINESS_SYSTEMS"
            }
        ]
    },
    {
        "language": "Q",
        "frameworks": [
            {
                "name": "Q Programming",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Qpav",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "R Programming",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Matlab",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "KDB+",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    # Compiled
    # A compiled language is a programming language whose implementations are typically compilers (translators that
    # generate machine code from source code), and not interpreters (step-by-step executors of source code, where no
    # pre-runtime translation takes place). (Wikipedia)
    {
        "language": "Ada",
        "frameworks": [
            {
                "name": "GNAT",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Ravenscar",
                "application_area": "REAL_TIME_SYSTEMS"
            },
            {
                "name": "SPARK",
                "application_area": "FORMAL_VERIFICATION"
            },
            {
                "name": "AdaCore",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "GLADE",
                "application_area": "DISTRIBUTED_SYSTEMS"
            }
        ]
    },
    {
        "language": "ALGOL",
        "frameworks": [
            {
                "name": "ALGOL W",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Simula",
                "application_area": "SIMULATION"
            },
            {
                "name": "Pascal",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "C",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Fortran",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "C",
        "frameworks": [
            {
                "name": "GCC",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "Clang",
                "application_area": "SYSTEMS_PROGRAMMING"
            },
            {
                "name": "LLVM",
                "application_area": "COMPILERS"
            },
            {
                "name": "CMake",
                "application_area": "BUILD_SYSTEMS"
            },
            {
                "name": "Emscripten",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "C++",
        "frameworks": [
            {
                "name": "Qt",
                "application_area": "GUI_DEVELOPMENT"
            },
            {
                "name": "Boost",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Poco",
                "application_area": "NETWORKING"
            },
            {
                "name": "Cinder",
                "application_area": "MULTIMEDIA"
            },
            {
                "name": "JUCE",
                "application_area": "AUDIO_PROCESSING"
            }
        ]
    },
    {
        "language": "C#",
        "frameworks": [
            {
                "name": "ASP.NET",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Blazor",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Entity Framework",
                "application_area": "DATABASE_MANAGEMENT"
            },
            {
                "name": "NancyFx",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Orleans",
                "application_area": "DISTRIBUTED_SYSTEMS"
            }
        ]
    },
    {
        "language": "CLEO",
        "frameworks": [
            {
                "name": "CLEO IDE",
                "application_area": "SOFTWARE_DEVELOPMENT"
            },
            {
                "name": "CLEO Compiler",
                "application_area": "COMPILERS"
            },
            {
                "name": "SIL",
                "application_area": "SOFTWARE_ENGINEERING"
            },
            {
                "name": "MODSIM",
                "application_area": "SIMULATION"
            },
            {
                "name": "Cytoscape",
                "application_area": "DATA_ANALYSIS"
            }
        ]
    },
    {
        "language": "COBOL",
        "frameworks": [
            {
                "name": "OpenCOBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "TinyCOBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "Micro Focus COBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "RM/COBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "COBOL-IT",
                "application_area": "BUSINESS_SYSTEMS"
            }
        ]
    },
    {
        "language": "Cobra",
        "frameworks": [
            {
                "name": "Cobra Compiler",
                "application_area": "COMPILERS"
            },
            {
                "name": "Cobra IDE",
                "application_area": "SOFTWARE_DEVELOPMENT"
            },
            {
                "name": "Mono",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Microsoft.NET",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Python.NET",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "D",
        "frameworks": [
            {
                "name": "Vibe.d",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Hunt",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Dplug",
                "application_area": "AUDIO_PROCESSING"
            },
            {
                "name": "DlangUI",
                "application_area": "GUI_DEVELOPMENT"
            },
            {
                "name": "Magpie",
                "application_area": "GENERAL_PURPOSE"
            }
        ]
    },
    {
        "language": "DASL",
        "frameworks": [
            {
                "name": "Apache NiFi",
                "application_area": "DATA_INTEGRATION"
            },
            {
                "name": "DataWeave",
                "application_area": "DATA_TRANSFORMATION"
            },
            {
                "name": "Clojure",
                "application_area": "GENERAL_PURPOSE"
            },
            {
                "name": "Ballerina",
                "application_area": "INTEGRATION"
            },
            {
                "name": "XSLT",
                "application_area": "DATA_TRANSFORMATION"
            }
        ]
    },
    {
        "language": "DIBOL",
        "frameworks": [
            {
                "name": "OpenDIBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "Synergy DBL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "DataFlex",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "ACUCOBOL",
                "application_area": "BUSINESS_SYSTEMS"
            },
            {
                "name": "Micro Focus Visual COBOL",
                "application_area": "BUSINESS_SYSTEMS"
            }
        ]
    },
    {
        "language": "Fortran",
        "frameworks": [
            {
                "name": "GNU Fortran",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "Intel Fortran",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "OpenMP",
                "application_area": "PARALLEL_COMPUTING"
            },
            {
                "name": "Fortran90",
                "application_area": "SCIENTIFIC_COMPUTING"
            },
            {
                "name": "NAG Fortran",
                "application_area": "SCIENTIFIC_COMPUTING"
            }
        ]
    },
    {
        "language": "Java",
        "frameworks": [
            {
                "name": "Spring",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Hibernate",
                "application_area": "ORM"
            },
            {
                "name": "Struts",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Vaadin",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "JSF",
                "application_area": "WEB_DEVELOPMENT"
            }
        ]
    },
    {
        "language": "JOVIAL",
        "frameworks": [
            {
                "name": "JOVIAL Compiler System",
                "application_area": "COMPILERS"
            },
            {
                "name": "Micro Focus JOVIAL",
                "application_area": "COMPILERS"
            },
            {
                "name": "JOVIAL IDE",
                "application_area": "SOFTWARE_DEVELOPMENT"
            },
            {
                "name": "GNATPro",
                "application_area": "COMPILERS"
            },
            {
                "name": "Ada",
                "application_area": "SYSTEMS_PROGRAMMING"
            }
        ]
    },
    {
        "language": "Objective-C",
        "frameworks": [
            {
                "name": "Cocoa Touch",
                "application_area": "MOBILE_DEVELOPMENT"
            },
            {
                "name": "Core Data",
                "application_area": "DATA_PERSISTENCE"
            },
            {
                "name": "AFNetworking",
                "application_area": "NETWORKING"
            },
            {
                "name": "Cocos2d",
                "application_area": "GAME_DEVELOPMENT"
            },
            {
                "name": "Xcode",
                "application_area": "IDE"
            }
        ]
    },
    {
        "language": "SMALL",
        "frameworks": []
    },
    {
        "language": "Smalltalk",
        "frameworks": [
            {
                "name": "Squeak",
                "application_area": "EDUCATION"
            },
            {
                "name": "Pharo",
                "application_area": "DEVELOPMENT"
            },
            {
                "name": "GemStone",
                "application_area": "DATABASE"
            },
            {
                "name": "Cincom Smalltalk",
                "application_area": "DEVELOPMENT"
            },
            {
                "name": "GNU Smalltalk",
                "application_area": "OPEN_SOURCE"
            }
        ]
    },
    {
        "language": "Simula",
        "frameworks": [
            {
                "name": "BETA",
                "application_area": "OBJECT_ORIENTED_PROGRAMMING"
            },
            {
                "name": "Mjølner",
                "application_area": "DEVELOPMENT"
            },
            {
                "name": "Object-Oriented Simula",
                "application_area": "OBJECT_ORIENTED_PROGRAMMING"
            },
            {
                "name": "Simula-67",
                "application_area": "OBJECT_ORIENTED_PROGRAMMING"
            },
            {
                "name": "Simscript",
                "application_area": "SIMULATION"
            }
        ]
    },
    {
        "language": "Swift",
        "frameworks": [
            {
                "name": "Vapor",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Kitura",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "Perfect",
                "application_area": "WEB_DEVELOPMENT"
            },
            {
                "name": "SwiftUI",
                "application_area": "UI_DEVELOPMENT"
            },
            {
                "name": "Alamofire",
                "application_area": "NETWORKING"
            }
        ]
    },
    {
        "language": "Turing",
        "frameworks": []
    },
    {
        "language": "Visual Basic",
        "frameworks": []
    },
    {
        "language": "Visual FoxPro",
        "frameworks": []
    },
    {
        "language": "XL",
        "frameworks": []
    },

    # Procedural
    # A compiled language is a programming language whose implementations are typically compilers (translators that
    # generate machine code from source code), and not interpreters (step-by-step executors of source code, where no
    # pre-runtime translation takes place). (Wikipedia)
    {
        "language": "Bliss",
        "frameworks": []
    },
    {
        "language": "ChucK",
        "frameworks": []
    },
    {
        "language": "CLIST",
        "frameworks": []
    },
    {
        "language": "HyperTalk",
        "frameworks": []
    },
    {
        "language": "Modula-2",
        "frameworks": []
    },
    {
        "language": "Oberon",
        "frameworks": []
    },
    {
        "language": "Component Pascal",
        "frameworks": []
    },
    {
        "language": "MATLAB",
        "frameworks": []
    },
    {
        "language": "Occam",
        "frameworks": []
    },
    {
        "language": "PL/C",
        "frameworks": []
    },
    {
        "language": "PL/I",
        "frameworks": []
    },
    {
        "language": "Rapira",
        "frameworks": []
    },
    {
        "language": "RPG",
        "frameworks": []
    },
    # Scripting Languages
    # Scripting languages are programming languages that control an application. Scripts can execute independent of any
    # other application. They are mostly embedded in the application that they control and are used to automate frequently
    # executed tasks like communicating with external programs.
    {
        "language": "AppleScript",
        "frameworks": []
    },
    {
        "language": "BeanShell",
        "frameworks": []
    },
    {
        "language": "ColdFusion",
        "frameworks": []
    },
    {
        "language": "F-Script",
        "frameworks": []
    },
    {
        "language": "JASS",
        "frameworks": []
    },
    {
        "language": "Maya Embedded Language",
        "frameworks": []
    },
    {
        "language": "Mondrian",
        "frameworks": []
    },
    {
        "language": "PHP",
        "frameworks": []
    },
    {
        "language": "Revolution",
        "frameworks": []
    },
    {
        "language": "Tcl",
        "frameworks": []
    },
    {
        "language": "VBScript",
        "frameworks": []
    },
    {
        "language": "Windows PowerShell",
        "frameworks": []
    },
    # Markup Languages
    # A markup language is an artificial language that uses annotations to text that define how the text is to be
    # displayed.
    {
        "language": "Curl",
        "frameworks": []
    },
    {
        "language": "SGML",
        "frameworks": []
    },
    {
        "language": "HTML",
        "frameworks": []
    },
    {
        "language": "XML",
        "frameworks": []
    },
    {
        "language": "XHTML",
        "frameworks": []
    },
    # Logic-based Programming Languages
    # Logic programming is a type of programming paradigm which is largely based on formal logic. Any program written in a
    # logic programming language is a set of sentences in logical form, expressing facts and rules about some problem
    # domain. (Wikipedia)
    {
        "language": "ALF",
        "frameworks": []
    },
    {
        "language": "Fril",
        "frameworks": []
    },
    {
        "language": "Janus",
        "frameworks": []
    },
    {
        "language": "Leda",
        "frameworks": []
    },
    {
        "language": "Oz",
        "frameworks": []
    },
    {
        "language": "Poplog",
        "frameworks": []
    },
    {
        "language": "Prolog",
        "frameworks": []
    },
    {
        "language": "ROOP",
        "frameworks": []
    },

    # Concurrent Programming Languages
    # Concurrent programming is a computer programming technique that provides for the execution of operations
    # concurrently — either within a single computer, or across a number of systems.In the latter case, the term
    # distributed computing is used.(Wikipedia)
    {
        "language": "ABCL",
        "frameworks": []
    },
    {
        "language": "Afnix",
        "frameworks": []
    },
    {
        "language": "Cilk",
        "frameworks": []
    },
    {
        "language": "Concurrent Pascal",
        "frameworks": []
    },
    {
        "language": "E",
        "frameworks": []
    },
    {
        "language": "Joule",
        "frameworks": []
    },
    {
        "language": "Limbo",
        "frameworks": []
    },
    {
        "language": "Pict",
        "frameworks": []
    },
    {
        "language": "SALSA",
        "frameworks": []
    },
    {
        "language": "SR",
        "frameworks": []
    },
    # Object-Oriented Programming Languages
    # Object-oriented programming (OOP) is a programming paradigm based on the concept of “objects”, which may contain
    # data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.
    # In OOP, computer programs are designed by making them out of objects that interact with one another. (Wikipedia)
    {
        "language": "Agora",
        "frameworks": []
    },
    {
        "language": "BETA",
        "frameworks": []
    },
    {
        "language": "Cecil",
        "frameworks": []
    },
    {
        "language": "Lava",
        "frameworks": []
    },
    {
        "language": "Lisaac",
        "frameworks": []
    },
    {
        "language": "MOO",
        "frameworks": []
    },
    {
        "language": "Moto",
        "frameworks": []
    },
    {
        "language": "Object-Z",
        "frameworks": []
    },
    {
        "language": "Obliq",
        "frameworks": []
    },
    {
        "language": "Oxygene",
        "frameworks": []
    },
    {
        "language": "Pliant",
        "frameworks": []
    },
    {
        "language": "Prograph",
        "frameworks": []
    },
    {
        "language": "REBOL",
        "frameworks": []
    },
    {
        "language": "Scala",
        "frameworks": []
    },
    {
        "language": "Self",
        "frameworks": []
    },
    {
        "language": "Slate",
        "frameworks": []
    },
    {
        "language": "XOTcl",
        "frameworks": []
    },
    {
        "language": "IO",
        "frameworks": []
    },

    # SQL Databases
    {
        "database": "PostgreSQL",
        "frameworks": []
    },
    {
        "database": "MySQL",
        "frameworks": []
    },
    {
        "database": "SQLite",
        "frameworks": []
    },
    {
        "database": "Microsoft SQL Server",
        "frameworks": []
    },
    {
        "database": "Oracle",
        "frameworks": []
    },
    {
        "database": "MariaDB",
        "frameworks": []
    },
    {
        "database": "SAP HANA",
        "frameworks": []
    },
    {
        "database": "Amazon Aurora",
        "frameworks": []
    },
    {
        "database": "Apache Derby",
        "frameworks": []
    },
    {
        "database": "CockroachDB",
        "frameworks": []
    },
    {
        "database": "ClickHouse",
        "frameworks": []
    },
    {
        "database": "Greenplum",
        "frameworks": []
    },
    {
        "database": "IBM Db2",
        "frameworks": []
    },
    {
        "database": "Teradata",
        "frameworks": []
    },
    {
        "database": "Firebird",
        "frameworks": []
    },
    {
        "database": "VoltDB",
        "frameworks": []
    },
    {
        "database": "TiDB",
        "frameworks": []
    },
    {
        "database": "Netezza",
        "frameworks": []
    },
    {
        "database": "SQL Azure",
        "frameworks": []
    },
    # NoSQL Databases
    {
        "database": "MongoDB",
        "frameworks": []
    },
    {
        "database": "Cassandra",
        "frameworks": []
    },
    {
        "database": "Redis",
        "frameworks": []
    },
    {
        "database": "CouchDB",
        "frameworks": []
    },
    {
        "database": "RethinkDB",
        "frameworks": []
    },
    {
        "database": "Google Cloud Firestore",
        "frameworks": []
    },
    {
        "database": "Azure Cosmos DB",
        "frameworks": []
    },
    {
        "database": "Neo4J",
        "frameworks": []
    },
    {
        "database": "ArangoDB",
        "frameworks": []
    },
    {
        "database": "OrientDB",
        "frameworks": []
    },
    {
        "database": "Couchbase",
        "frameworks": []
    },
    {
        "database": "ScyllaDB",
        "frameworks": []
    },
    {
        "database": "Amazon DynamoDB",
        "frameworks": []
    },
    {
        "database": "Elasticsearch",
        "frameworks": []
    },
]


def seed_languages_and_frameworks(db: Session):
    for lang_data in technologies_data:
        existing_lang = db.query(Language).filter(Language.name == lang_data["language"]).first()
        if not existing_lang:
            language = Language(name=lang_data["language"])
            db.add(language)
            db.commit()
            db.refresh(language)

            for framework_data in lang_data["frameworks"]:
                framework = Framework(
                    name=framework_data["name"],
                    language_id=language.language_id,
                    application_area=framework_data.get("application_area")
                )
                db.add(framework)

            db.commit()
        else:
            print(f"Language {lang_data['language']} already exists in the database.")


def main():
    db = SessionLocal()
    try:
        seed_languages_and_frameworks(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
