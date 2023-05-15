import PySimpleGUI as sg

from .theme import THEME

sg.theme(THEME)


def stat_box(stat_name: str, size=(5, 1)):
    return sg.Text(
        "0",
        key=stat_name,
        relief=sg.RELIEF_SUNKEN,
        text_color="blue",
        size=size,
    )


stats_title = [
    [
        [
            sg.Text("workbench_starts: "),
        ],
        [
            sg.Text("workbench_collects"),
        ],
        [
            sg.Text("bitcoin_collects"),
        ],
        [
            sg.Text("lavatory_starts"),
        ],
        [
            sg.Text("lavatory_collects"),
        ],
    ],
    [
        [
            sg.Text("medstation_starts"),
        ],
        [
            sg.Text("medstation_collects"),
        ],
        [
            sg.Text("water_filters"),
        ],
        [
            sg.Text("water_collects"),
        ],
        [
            sg.Text("restarts"),
        ],
    ],
]


stats_values = [
    [
        [
            stat_box("workbench_starts"),
        ],
        [
            stat_box("workbench_collects"),
        ],
        [
            stat_box("bitcoin_collects"),
        ],
        [
            stat_box("lavatory_starts"),
        ],
        [
            stat_box("lavatory_collects"),
        ],
    ],
    [
        [
            stat_box("medstation_starts"),
        ],
        [
            stat_box("medstation_collects"),
        ],
        [
            stat_box("water_filters"),
        ],
        [
            stat_box("water_collects"),
        ],
        [
            stat_box("restarts"),
        ],
    ],
]

stats = [
    [
        sg.Column(stats_title[0], element_justification="right"),
        sg.Column(stats_values[0], element_justification="left"),
        sg.Column(stats_title[1], element_justification="right"),
        sg.Column(stats_values[1], element_justification="left"),
    ]
]
