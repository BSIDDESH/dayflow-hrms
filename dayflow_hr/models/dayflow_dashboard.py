<odoo>

    <record id="view_dayflow_dashboard_list" model="ir.ui.view">
        <field name="name">dayflow.dashboard.list</field>
        <field name="model">dayflow.dashboard</field>
        <field name="arch" type="xml">
            <list string="Employee Dashboard">
                <field name="employee_id"/>
                <field name="attendance_status"/>
                <field name="pending_leaves"/>
                <field name="approved_leaves"/>
            </list>
        </field>
    </record>

    <record id="view_dayflow_dashboard_form" model="ir.ui.view">
        <field name="name">dayflow.dashboard.form</field>
        <field name="model">dayflow.dashboard</field>
        <field name="arch" type="xml">
            <form string="Employee Dashboard">
                <header>
                    <button name="compute_summary" string="Refresh Data" type="object" class="oe_highlight"/>
                </header>
                <sheet>
                    <group>
                        <field name="employee_id"/>
                        <field name="attendance_status"/>
                        <field name="pending_leaves"/>
                        <field name="approved_leaves"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_dayflow_dashboard" model="ir.actions.act_window">
        <field name="name">Employee Dashboard</field>
        <field name="res_model">dayflow.dashboard</field>
        <field name="view_mode">list,form</field>
    </record>

    <menuitem id="menu_dayflow_dashboard_root"
              name="Dayflow Dashboard"
              sequence="10"/>

    <menuitem id="menu_dayflow_dashboard"
              name="Employee Dashboard"
              parent="menu_dayflow_dashboard_root"
              action="action_dayflow_dashboard"
              sequence="10"/>

</odoo>