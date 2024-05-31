import { Layout } from "antd"
import * as cls from "./MainPage.module.scss"
import Logo from "../assets/logo.png"
import { Logs } from "widgets/Logs"

const { Header, Content } = Layout

export const MainPage = () => {
    return (
        <Layout style={{height: "100vh"}}>
            <Header className={cls.header}>
                <img src={Logo} className={cls.logo} alt="logo" />
            </Header>
            <Content>
                <Logs/>
            </Content>
        </Layout>
    )
}

