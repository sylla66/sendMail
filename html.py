from js import obtenir_classe_couleur, obtenir_fleche_et_couleur
from style import ajouter_styles_simple



def code_html():
    return f"""
                        <html>
                          <head>
                           {ajouter_styles_simple()}
                          </head>
                          <body>
                                <h5>Beautiful tables 2 templates with only html/css/JS</h5>
                                <table class="content-table">
                                    <thead>
                                        <tr>
                                            <th class="transparent"></th>
                                            <th class="not-transparent">août-23</th>
                                            <th class="not-transparent">sept-23</th>
                                            <th class="single-color">%MoM</th>
                                        </tr>
                                    </thead>
                                    <tbody>

                                        <tr>
                                            <td>JAMONO ALLO</td>
                                            <td>2 196 799</td>
                                            <td>2 198 071</td>
                                            <td class="{obtenir_classe_couleur(5767)}">5767% 
                                            {obtenir_fleche_et_couleur(5767)}</td>
                                        </tr>
                                        <tr>
                                            <td>JAMONO MAX</td>
                                            <td>102 553</td>
                                            <td>105 238</td>
                                            <td class="{obtenir_classe_couleur(0)}">0% 
                                            {obtenir_fleche_et_couleur(0)}</td>
                                        </tr>
                                        <tr>
                                            <td>JAMONO NEW S'COOL</td>
                                            <td>1 836 554</td>
                                            <td>1 890 256</td>
                                            <td class="{obtenir_classe_couleur(-8)}">-8% 
                                            {obtenir_fleche_et_couleur(-8)}</td>
                                        </tr>
                                        <tr>
                                            <td>JAMONO PRO</td>
                                            <td>490 187</td>
                                            <td>462 229</td>
                                            <td class="{obtenir_classe_couleur(-6)}">{-6}% 
                                            {obtenir_fleche_et_couleur(-6)}</td>
                                        </tr>
                                        <tr>
                                            <td>KIRENE AVEC ORANGE</td>
                                            <td>3 517 148</td>
                                            <td>3 559 137</td>
                                            <td class="{obtenir_classe_couleur(1)}">1% 
                                            {obtenir_fleche_et_couleur(1)}</td>
                                        </tr>
                                        <tr class="total">
                                            <td>Total</td>
                                            <td>8 143 241</td>
                                            <td>8 214 931</td>
                                            <td class="{obtenir_classe_couleur(10)}">{10}% 
                                            {obtenir_fleche_et_couleur(10)}</td>
                                        </tr>
                                    </tbody>
                                </table>
                                <h5>Beautiful tables 1 templates with only html/css/JS</h5>
                                <table class="content-table">
                                    <tbody>
                                        <tr>
                                            <td colspan="4" class="diff">Jeune</td>
                                            <td>539 052</td>
                                            <td>429 577</td>
                                            <td class="{obtenir_classe_couleur(56)}">{56}% 
                                            {obtenir_fleche_et_couleur(56)}</td>
                                        </tr>
                                        <tr>
                                            <td colspan="4" class="diff">Non Jeune</td>
                                            <td>55 538</td>
                                            <td>40 969</td>
                                            <td class="{obtenir_classe_couleur(-26)}">{-26}% 
                                            {obtenir_fleche_et_couleur(-26)}</td>
                                        </tr>
                                        <tr class="total">
                                            <td colspan="4">Total</td>
                                            <td>594 590</td>
                                            <td>470 546</td>
                                            <td class="{obtenir_classe_couleur(-1)}">{-1}% 
                                            {obtenir_fleche_et_couleur(-1)}</td>
                                        </tr>
                                    </tbody>
                                </table>

                            </body>
                        </html>
            """