import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            # dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
            # dbc.NavItem(dbc.NavLink("About", href="/about")),
            # dbc.NavItem(dbc.NavLink("Trial", href="/trial")),
            dbc.NavItem(dbc.NavLink("Blog", href="https://medium.com/@socjon")),
            dbc.NavItem(dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/tyler-jonathan/")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Portfolio",
                children=[
                    dbc.DropdownMenuItem("Auditors Aid", href="/projects"),
                    dbc.DropdownMenuItem("Entry 2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Entry 3"),
                ],
            ),
        ],
        brand="About",
        brand_href="/about",
        sticky="top",
    )
    return navbar
