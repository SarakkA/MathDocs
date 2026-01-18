# Equazioni di secondo grado complete

Le equazioni complete hanno la forma:

$$ax^2 + bx + c = 0$$

Si risolvono con la **formula quadratica**:

$$x_{1,2} = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Di solito, si calcola prima il numero sotto radice

questa quantità viene chiamata **Delta** $\Delta = b^2 - 4ac$

=== "Esempio 1 – Due soluzioni"

    $$x^2 + 2x - 3 = 0$$

    Si calcola il Delta:

    $$
    \begin{aligned}
    \Delta &= b^2 - 4ac \\
    &= 2^2 - 4(1)(-3) \\
    &= 4 + 12 \\
    &= 16 \\
    \end{aligned}
    $$

    Si inserisce nella formula

    $$
    x_{1,2} = \frac{-2 \pm \sqrt{16}}{2}
    = \frac{-2 \pm 4}{2}
    =\begin{cases}
	\displaystyle\frac{-2+4}{2}=1\\
    \displaystyle\frac{-2-4}{2}=-3
	\end{cases}
    $$

    $$
    x_1 = 1 \qquad x_2 = -3
    $$

    !!! tip "Nota"
        Se $\Delta > 0$ l'equazione ha **sempre due soluzioni**

=== "Esempio 2 – Soluzione doppia"

    $$2x^2 - 4x + 2 = 0$$

    $$
    \begin{aligned}
    \Delta &= b^2 - 4ac \\
    &= (-4)^2 - 4(2)(2) \\
    &= 16-16 \\
    &= 0 \\
    \end{aligned}
    $$

    $$
    x_{1,2} = \frac{4 \pm \sqrt{0}}{4} = 1
    $$

    !!! tip "Nota"
        Se $\Delta = 0$ l'equazione ha **una sola soluzione**

=== "Esempio 3 – Nessuna soluzione"

    $$-x^2 + 2x - 2 = 0$$

    $$
    \begin{aligned}
    \Delta &= b^2 - 4ac \\
    &= 2^2 - 4(-1)(-2) \\
    &= 4-8 \\
    &= -4 \\
    \end{aligned}
    $$

    Non possiamo calcolare la radice quadrata di $\Delta$

    !!! warning "Nota" 
        Se $\Delta < 0$ l'equazione è **impossibile**


---

<div style="text-align: right;">
  <a href="../esercizi/" class="md-button md-button--primary">
    Esercizi →
  </a>
</div>