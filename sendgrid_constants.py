quotes_unpaid_from_email = "martin@tinytiny.dk"
quotes_unpaid_to_email = "gertrud@tinytiny.dk"
quotes_unpaid_cc_email = "martin@tinytiny.dk"
quotes_unpaid_subject = "Forladt indkøbskurv {created_at:%Y-%m-%d %H:%M}"
quotes_unpaid_content = ("<html>"
                         "<body>"
                         "<b>Kunde email:</b> {customer_email}<br/>"
                         "<b>Kunde navn:</b> {customer_firstname} {customer_lastname}<br/>"
                         "<br/>"
                         "<b>Ordrestørrelse:</b> {base_currency_code} {base_grand_total:.2f}<br/>"
                         "<br/>"
                         "{quote_items}")
quote_unpaid_item = ("<tr>"
                     "<td>{sku}</td>"
                     "<td>{name}</td>"
                     "<td>{qty:.0f}</td>"
                     "<td>{base_row_total:.2f}</td>"
                     "</tr>")