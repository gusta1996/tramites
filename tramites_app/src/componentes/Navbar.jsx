import React from 'react';
import { Menu } from 'semantic-ui-react'

export const Navbar = () =>{
    return (
        <Menu pointing style={{margin:'0px', height:'calc(10vh)'}}>
            <Menu.Item  name='Logo' href="/somelink"/>
            <Menu.Item  name='Registrese' href="/somelink"/>
            <Menu.Item  name='Iniciar Sesión' href="/somelink"/>
        </Menu>
    )
}