from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    background_image = fields.Binary(string="Jazzy Background Image", attachment=True)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    theme_background = fields.Binary(string="App menu Background",
                                     related='company_id.background_image',
                                     readonly=False)

    app_bar_color = fields.Char(string='Appbar color',
                                config_parameter='jazzy_backend_theme.appbar_color',
                                default='#212529')
    primary_accent = fields.Char(string="Navbar Background Color",
                                 config_parameter='jazzy_backend_theme.primary_accent_color',
                                 default='#0874AA')
    secondary_accent = fields.Char(string="Primary Border Color",
                                   config_parameter='jazzy_backend_theme.secondary_color',
                                   default='#065379')

    kanban_bg_color = fields.Char(string="Kanban Bg Color",
                                  config_parameter='jazzy_backend_theme.kanban_bg_color',
                                  default='#F7F7F7')

    primary_hover = fields.Char(string="Hover Primary Color",
                                config_parameter='jazzy_backend_theme.primary_hover',
                                default='#00376e')
    light_hover = fields.Char(string="Light Hover",
                              config_parameter='jazzy_backend_theme.light_hover',
                              default='#d5d5d5')
    appbar_text = fields.Char(string="Home Menu Text Color",
                              config_parameter='jazzy_backend_theme.appbar_text',
                              default='#04405E')
    secoundary_hover = fields.Char(string="AppBar Hover",
                                   config_parameter='jazzy_backend_theme.secoundary_hover',
                                   default='#ffffff')

    def config_color_settings(self):
        colors = {}
        #print("ppp", self.env.user.company_id.background_image)
        colors['full_bg_img'] = self.env.user.company_id.background_image
        colors['appbar_color'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.appbar_color');
        colors['primary_accent'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.primary_accent_color');
        colors['secondary_color'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.secondary_color');
        colors['kanban_bg_color'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.kanban_bg_color');
        colors['primary_hover'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.primary_hover');
        colors['light_hover'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.light_hover');
        colors['appbar_text'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.appbar_text');
        colors['secoundary_hover'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'jazzy_backend_theme.secoundary_hover');

        return colors
