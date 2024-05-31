import classNames  from 'classnames';
import * as cls from './AnimatedRow.module.scss';
import { useSpring, animated } from '@react-spring/web';
interface AnimatedRowProps {
    children?: React.ReactNode
}

export const AnimatedRow = ({children, ...props}: AnimatedRowProps) => {
   const styles = useSpring({
       from: {opacity: 0},
       to: {opacity: 1},
   })
    return (
        <animated.tr style={styles} {...props} >
            {children}
        </animated.tr>
    );
}

