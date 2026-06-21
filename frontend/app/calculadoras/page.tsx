"use client";

import { useState } from "react";

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
  const [codigoSelecionado, setCodigoSelecionado] = useState(
  "produtividade_simples"
);
const calculadoraSelecionada = calculadoras.find(
  (calculadora) => calculadora.codigo === codigoSelecionado) ??
  calculadoras[0];

  return (
    <main className="min-h-screen bg-gradient-to-br from-[#2f3522] via-[#505431] to-[#6f6840] text-stone-950">
      <section className="mx-auto max-w-6xl px-6 py-16">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.3em] text-[#e7e0cb]">
          AgroRock
        </p>

        <h1 className="text-4xl font-bold tracking-tight text-stone-950 text-[#f4f1e8] sm:text-5xl">
          Calculadoras agronômicas
        </h1>

        <p className="mt-4 max-w-2xl text-lg leading-8 text-[#ded6c3]">
          Ferramentas simples para organizar cálculos técnicos do dia a dia no campo. O
          sistema calcula; o agrônomo decide.
        </p>

        <div className="mt-10 grid gap-6 lg:grid-cols-[280px_1fr]">
          <aside className="space-y-3">
  
            {calculadoras.map((calculadora) => (
              <button
                key={calculadora.codigo}
                onClick={() => setCodigoSelecionado(calculadora.codigo)}
                className="w-full rounded-xl border border-stone-300 bg-[#f4f1e8] px-4 py-3 text-left transition hover:border-green-900 hover:bg-[#fbfaf5]"
>

                <span className="block text-sm font-semibold text-stone-950">
                  {calculadora.nome}
                </span>

                <span className="mt-1 block text-xs uppercase tracking-wide text-green-800">
                  {calculadora.categoria}
                </span>
            </button>
        ))}
        </aside>
        <section className="rounded-2xl border border-stone-300 bg-[#f4f1e8] p-6 shadow-sm">
  <p className="text-sm font-semibold uppercase tracking-wide text-green-800">
    Calculadora selecionada
  </p>

  <h2 className="mt-3 text-3xl font-bold text-stone-950">
    {calculadoraSelecionada.nome}
  </h2>

  <p className="mt-3 max-w-2xl text-stone-700">
    {calculadoraSelecionada.descricao}
  </p>

  <div className="mt-8 grid gap-4 md:grid-cols-3">
    <div>
      <label className="text-sm font-medium text-stone-700">
        Peso total colhido
      </label>
      <div className="mt-2 rounded-xl border border-stone-300 bg-white px-4 py-3 text-stone-500">
        kg
      </div>
    </div>

    <div>
      <label className="text-sm font-medium text-stone-700">
        Área colhida
      </label>
      <div className="mt-2 rounded-xl border border-stone-300 bg-white px-4 py-3 text-stone-500">
        hectares
      </div>
    </div>

    <div>
      <label className="text-sm font-medium text-stone-700">
        Peso da saca
      </label>
      <div className="mt-2 rounded-xl border border-stone-300 bg-white px-4 py-3 text-stone-500">
        kg
      </div>
    </div>
  </div>

  <button className="mt-8 rounded-xl bg-green-900 px-5 py-3 font-semibold text-white transition hover:bg-green-800">
    Calcular produtividade
  </button>

  <div className="mt-8 rounded-2xl border border-green-900/20 bg-green-950/5 p-5">
    <p className="text-sm font-semibold uppercase tracking-wide text-green-900">
      Resultado técnico
    </p>

    <p className="mt-3 text-stone-700">
      Aguardando dados para cálculo.
    </p>
  </div>
</section>
        </div>
      </section>
    </main>
  );
}