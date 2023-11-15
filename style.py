
def ajouter_styles_simple():
    return """
    <style>
        .positif { color: green; }
        .negatif { color: red; }

        .content-table {
                                border-collapse: collapse;
                                margin: 25px 0;
                                font-size: 0.9em;
                                min-width: 400px;
                                border-radius: 4px 4px 0 0;
                                overflow: hidden;
                                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                font-family: Arial, Helvetica, sans-serif;
                            }

                            .content-table thead tr {
                                text-align: left;
                                font-weight: bold;
                            }

                            .content-table thead th.transparent {
                                background-color: transparent;
                            }

                            .content-table thead th.not-transparent {
                                background-color: purple;
                                color: #fff;
                            }

                            .content-table thead th.single-color {
                                background-color: #fc7c04;
                                color: #fff;
                            }

                            .content-table th,
                            .content-table td {
                                padding: 8px 10px;
                            }

                            .content-table td.diff {
                                background-color: #dce6eb;
                            }

                            .content-table td.kpi-up {
                                color: green;
                            }

                            .content-table td.kpi-down {
                                color: red;
                            }

                            .content-table tbody tr {
                                border-bottom: 1px solid #dddddd;
                            }


                            .content-table tbody tr:last-of-type {
                                border-bottom: 2px solid #fc7c04;
                            }

                            .content-table tbody tr.total{
                                font-weight: bold;
                                background-color: #d9d9d9;
                            }
    </style>
    """