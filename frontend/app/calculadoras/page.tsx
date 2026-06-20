const calculadoras = [
  {
    codigo: "produtividade_simples",
    nome: "Produtividade simples",
    categoria: "Produtividade",
    descricao: "Calcula produtividade em kg/ha, t/ha e sacas/ha.",
  },
  {
    codigo: "volume_calda_simples",
    nome: "Volume de calda simples",
    categoria: "Aplicação",
    descricao:
      "Calcula o volume total de calda a partir da área e do volume por hectare.",
  },
  {
    codigo: "quantidade_produto_simples",
    nome: "Quantidade total de produto",
    categoria: "Aplicação",
    descricao:
      "Calcula a quantidade total de produto a partir da área e da dose por hectare.",
  },
  {
    codigo: "converter_m2_para_ha",
    nome: "Conversor de m² para hectares",
    categoria: "Conversão de área",
    descricao: "Converte uma área em metros quadrados para hectares.",
  },
  {
    codigo: "converter_ha_para_m2",
    nome: "Conversor de hectares para m²",
    categoria: "Conversão de área",
    descricao: "Converte uma área em hectares para metros quadrados.",
  },
];

export default function CalculadorasPage() {
  return (
    <main className="min-h-screen bg-zinc-950 text-zinc-100">
      <section className="mx-auto max-w-6xl px-6 py-16">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.3em] text-emerald-400">
          AgroRock
        </p>

        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
          Calculadoras agronômicas
        </h1>

        <p className="mt-4 max-w-2xl text-lg leading-8 text-zinc-300">
          Ferramentas simples para organizar cálculos técnicos do dia a dia no
          campo. O sistema calcula; o agrônomo decide.
        </p>

        <div className="mt-10 grid gap-5 md:grid-cols-2">
          {calculadoras.map((calculadora) => (
            <article
              key={calculadora.codigo}
              className="rounded-2xl border border-zinc-800 bg-zinc-900/70 p-6 transition hover:border-emerald-500/60"
            >
              <p className="text-sm font-medium text-emerald-400">
                {calculadora.categoria}
              </p>

              <h2 className="mt-3 text-2xl font-semibold">
                {calculadora.nome}
              </h2>

              <p className="mt-3 leading-7 text-zinc-300">
                {calculadora.descricao}
              </p>

              <button className="mt-6 rounded-xl bg-emerald-500 px-4 py-2 font-semibold text-zinc-950 transition hover:bg-emerald-400">
                Abrir calculadora
              </button>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}