import { mount } from '@vue/test-utils'
import AddrForm from '@/components/present/addr_form.vue'

describe('AddrForm', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(AddrForm)
    expect(wrapper.vm).toBeTruthy()
  })
})
