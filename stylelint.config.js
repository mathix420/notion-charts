module.exports = {
  extends: [
    'stylelint-config-standard-scss',
    'stylelint-config-recommended-vue',
    'stylelint-config-standard',
    'stylelint-config-prettier',
  ],
  // https://stylelint.io/user-guide/configuration
  rules: {
    'no-empty-source': null,
    'at-rule-no-unknown': null,
    'font-family-no-missing-generic-family-keyword': null,
    'selector-pseudo-element-no-unknown': [
      true,
      {
        ignorePseudoElements: ['v-deep'],
      },
    ],
  },
}
