
import { Avatar, Button, Table, TableProps, Tag } from 'antd';
import { useEffect, useRef, useState } from 'react';
import { $api } from 'shared/api/api';

import { LogSchema } from '../model/types/LogSchema';
import * as cls from './Logs.module.scss'
import { ArrowDownOutlined } from '@ant-design/icons';
interface LogsProps {
    className?: string
}
const dateOptions: Intl.DateTimeFormatOptions = {
    day: "numeric",
    month: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric"
}
const columns: TableProps<LogSchema>['columns'] = [
    {
        title: 'Фото',
        dataIndex: 'image',
        key: 'image',
        width: 100,
        render: (val) => <Avatar src={`https://4b1ee103-c4f7-4f1b-af2f-fade32f113d3.selstorage.ru/${val}`} size={64} />
    },
    {
        title: 'ID',
        dataIndex: 'face_id',
        key: 'face_id',
        width: 100,
        responsive: ['md'],
    },
    {
        title: 'Имя',
        width: 150,
        dataIndex: 'first_name',
        key: 'full_name',
        render: (val) => {if (val === null) return "-"; return val}
        },
    {
        title: 'Фамилия',
        width: 150,
        dataIndex: 'last_name',
        key: 'full_name',
        render: (val) => {if (val === null) return "-"; return val}
    },
    {
        title: 'Отчество',
        width: 150,
        dataIndex: 'patronymic',
        key: 'full_name',
        render: (val) => {if (val === null) return "-"; return val}
    },
    {
        title: 'Идентифицирован',
        key: 'is_identified',
        dataIndex: 'is_identified',
        width: 170,
        render: (val) => <Tag color={val ? 'green' : 'red'}>{val ? 'Да' : 'Нет'}</Tag>,
    },
    {
        title: 'Дата создания пропуска',
        dataIndex: 'pass_issue_date',
        key: 'pass_issue_date',
        width: 200,
        render: (val) => { if (val === null) return "-"; return new Date(val).toLocaleDateString("ru", dateOptions) },

    },
    {
        title: 'Срок действия пропуска',
        dataIndex: 'pass_expiration_date',
        key: 'pass_expiration_date',
        width: 200,
        render: (val) => { if (val === null) return "-"; return new Date(val).toLocaleDateString("ru", dateOptions) },
    },
    {
        title: 'Дата обнаружения',
        dataIndex: 'detection_date',
        key: 'detection_date',
        width: 200,
        render: (val) => { if (val === null) return "-"; return new Date(val).toLocaleDateString("ru", dateOptions) },
    },
]



export const Logs = ({ className }: LogsProps) => {
    const [data, setData] = useState<LogSchema[]>([])
    const tableRef = useRef(null)
    const [showScrollBtn, setShowScrollBtn] = useState(false)
    const socket = useRef<WebSocket>()
    useEffect(() => {
        // $api.get<LogSchema[]>('/logs').then((res) => {
        //     setData(res.data)
        //     setShowScrollBtn(true)
        // })
        socket.current = new WebSocket('ws://77.223.100.176:8081/realtime')
        socket.current.onopen = () => {
            console.log(123)

        }
        socket.current.onmessage = (event: MessageEvent) => {
            const message: LogSchema = JSON.parse(event.data)
            const tableBody = document.querySelector('.ant-table-body')
            const { scrollTop, scrollHeight, clientHeight } = tableBody
            const needToScroll = scrollHeight - scrollTop === clientHeight
            setData((prev) => [...prev, message])
            if(needToScroll) {
                tableBody.scrollTo({ top: tableBody.scrollHeight, behavior: 'smooth' }) }
        }
        socket.current.onclose = () => {
            console.log(321)
        }
        socket.current.onerror = (e) => {
            console.log(e)
        }
        return () => {
            socket.current?.close()
        }
    }, [])
    const handleClick = () => {
        const tableBody = document.querySelector('.ant-table-body')
        tableBody.scrollTo({ top: tableBody.scrollHeight, behavior: 'smooth' })
    }

    const handleScroll: TableProps<LogSchema>['onScroll'] = (e) => {
        // @ts-ignore
        const { scrollTop, scrollHeight, clientHeight } = e.target
        if (scrollHeight - scrollTop === clientHeight) {
            console.log(123)
            setShowScrollBtn(false)
        } else {
            setShowScrollBtn(true)
        }
    }
    return (
        <div style={{ position: 'relative' }}>
            <Table
                columns={columns}
                pagination={false}
                dataSource={data}
                rowClassName={cls.row}
                ref={tableRef}
                scroll={{ y: 500, x: '100%' }}
                className={cls.table}
                onScroll={handleScroll}
                locale={{ emptyText: 'Нет данных' }}
            />
            {showScrollBtn && <Button type='primary' size='large' shape='circle' icon={<ArrowDownOutlined />} className={cls.scrollBtn} onClick={() => handleClick()}></Button>}
        </div>
    );
}

