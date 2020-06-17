import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            # dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
            # dbc.NavItem(dbc.NavLink("About", href="/about")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Portfolio",
                children=[
                    dbc.DropdownMenuItem("Auditors Aid", href="/projects"),
                    dbc.DropdownMenuItem("How I built this site", href="/dash_101"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Entry 3"),
                ],
            ),
            dbc.NavItem(dbc.NavLink("Blog", href="https://medium.com/@socjon")),
            dbc.NavItem(dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/tyler-jonathan/")),

        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
    )
    return navbar
